# ../gungame/plugins/custom/gg_knife_advanced/rules.py

"""Creates the gg_knife_advanced rules."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.rules.instance import GunGameRules

# Plugin
from .info import info

# =============================================================================
# >> RULES
# =============================================================================
knife_advanced_rules = GunGameRules(info.name)
knife_advanced_rules.register_all_rules()
