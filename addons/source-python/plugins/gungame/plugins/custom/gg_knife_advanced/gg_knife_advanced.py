# ../gungame/plugins/custom/gg_knife_advanced/gg_knife_advanced.py

"""."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events.hooks import EventAction, PreEvent
from listeners.tick import Delay

# GunGame
from gungame.core.players.dictionary import player_dictionary

# Plugin
from .custom_events import GG_Level_Swapped


# =============================================================================
# >> GUNGAME PRE-EVENTS
# =============================================================================
@PreEvent('gg_knife_steal')
def _pre_knife_steal(game_event):
    previous_attacker_level = game_event['attacker_level'] - 1
    previous_victim_level = game_event['victim_level'] + 1
    difference = previous_victim_level - previous_attacker_level

    if difference <= 1:
        return EventAction.CONTINUE

    levels = abs(difference) - 1
    killer = player_dictionary[game_event['attacker']]
    victim = player_dictionary[game_event['victim']]

    Delay(
        delay=0,
        callback=killer.increase_level,
        kwargs={
            'levels': levels,
            'reason': 'swap',
            'victim': victim.userid,
        },
    )
    Delay(
        delay=0,
        callback=victim.decrease_level,
        kwargs={
            'levels': levels,
            'reason': 'swap',
            'attacker': killer.userid,
        }
    )
    Delay(
        delay=0,
        callback=_fire_swap_event,
        kwargs={
            'killer': killer.userid,
            'killer_level': previous_victim_level,
            'victim': victim.userid,
            'victim_level': previous_attacker_level,
        }
    )
    return EventAction.CONTINUE


@PreEvent('gg_level_up')
def _pre_level_up(game_event):
    if game_event['reason'] != 'steal':
        return EventAction.CONTINUE

    level = game_event['new_level']
    if level != game_event['old_level'] + 1:
        return EventAction.CONTINUE

    victim = player_dictionary[game_event['victim']]
    if victim.level <= level:
        return EventAction.CONTINUE

    return EventAction.BLOCK


@PreEvent('gg_level_down')
def _pre_level_down(game_event):
    if game_event['reason'] != 'steal':
        return EventAction.CONTINUE

    level = game_event['new_level']
    if level != game_event['old_level'] - 1:
        return EventAction.CONTINUE

    killer = player_dictionary[game_event['attacker']]
    if killer.level >= level:
        return EventAction.CONTINUE

    return EventAction.BLOCK


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _fire_swap_event(killer, killer_level, victim, victim_level):
    with GG_Level_Swapped() as event:
        event.attacker = event.leveler = killer
        event.attacker_level = killer_level
        event.userid = event.victim = victim
        event.victim_level = victim_level
