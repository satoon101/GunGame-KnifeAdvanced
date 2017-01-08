# ../gungame/plugins/custom/gg_knife_advanced/rules.py

"""Creates the gg_knife_advanced rules."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.rules.instance import GunGameRules
from gungame.core.rules.strings import rules_translations

# Plugin
from .info import info


# =============================================================================
# >> RULES
# =============================================================================
knife_advanced_rules = GunGameRules(info.name)
