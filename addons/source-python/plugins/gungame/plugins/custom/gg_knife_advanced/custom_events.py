# ../gungame/plugins/custom/gg_knife_advanced/custom_events.py

"""Events used by gg_knife_advanced."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events.custom import CustomEvent
from events.variable import ByteVariable, ShortVariable

# GunGame
from gungame.core.events.resource import GGResourceFile

# Plugin
from .info import info

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "GG_Level_Swapped",
)


# =============================================================================
# >> CLASSES
# =============================================================================
# ruff: noqa: N801
class GG_Level_Swapped(CustomEvent):
    """Called when a player steals a level by knifing."""

    attacker = leveler = ShortVariable(
        "The userid of the player that stole the level",
    )
    attacker_level = ByteVariable("The new level of the attacker")
    userid = victim = ShortVariable(
        "The userid of the player that had a level stolen",
    )
    victim_level = ByteVariable("The new level of the victim")


# =============================================================================
# >> RESOURCE FILE
# =============================================================================
GGResourceFile(info.name, GG_Level_Swapped)
