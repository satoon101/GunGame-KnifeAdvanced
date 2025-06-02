# ../gungame/plugins/custom/gg_knife_advanced/gg_knife_advanced.py

"""Plugin that allows players to swap levels when they steal."""

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
@PreEvent("gg_knife_steal")
def _pre_knife_steal(game_event):
    previous_attacker_level = game_event["attacker_level"] - 1
    previous_victim_level = game_event["victim_level"] + 1
    difference = previous_victim_level - previous_attacker_level
    if difference <= 1:
        return EventAction.CONTINUE

    Delay(
        delay=0,
        callback=_swap_player_levels,
        kwargs={
            "attacker": game_event["attacker"],
            "attacker_level": previous_victim_level,
            "victim": game_event["victim"],
            "victim_level": previous_attacker_level,
            "levels": abs(difference) - 1,
        },
    )
    return EventAction.CONTINUE


@PreEvent("gg_level_up")
def _pre_level_up(game_event):
    if game_event["reason"] != "steal":
        return EventAction.CONTINUE

    level = game_event["new_level"]
    if level != game_event["old_level"] + 1:
        return EventAction.CONTINUE

    victim = player_dictionary[game_event["victim"]]
    if victim.level <= level:
        return EventAction.CONTINUE

    return EventAction.BLOCK


@PreEvent("gg_level_down")
def _pre_level_down(game_event):
    if game_event["reason"] != "steal":
        return EventAction.CONTINUE

    level = game_event["new_level"]
    if level != game_event["old_level"] - 1:
        return EventAction.CONTINUE

    killer = player_dictionary[game_event["attacker"]]
    if killer.level >= level:
        return EventAction.CONTINUE

    return EventAction.BLOCK


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _swap_player_levels(attacker, attacker_level, victim, victim_level, levels):
    killer = player_dictionary[attacker]
    victim = player_dictionary[victim]
    killer.increase_level(
        levels=levels,
        reason="swap",
        victim=victim.userid,
        sound_name="swapped_up",
    )
    victim.decrease_level(
        levels=levels,
        reason="swap",
        attacker=attacker,
        sound_name="swapped_down",
    )
    with GG_Level_Swapped() as event:
        event.attacker = event.leveler = attacker
        event.attacker_level = attacker_level
        event.userid = event.victim = victim.userid
        event.victim_level = victim_level
