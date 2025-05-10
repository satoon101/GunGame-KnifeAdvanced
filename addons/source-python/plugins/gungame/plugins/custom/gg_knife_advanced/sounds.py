# ../gungame/plugins/custom/gg_knife_advanced/sounds.py

"""Register knife advanced sounds."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.sounds.manager import sound_manager

# =============================================================================
# >> SOUND REGISTRATION
# =============================================================================
sound_manager.register_sound(
    sound_name="swapped_up",
    default="source-python/gungame/default/smb3_1-up.mp3",
)

sound_manager.register_sound(
    sound_name="swapped_down",
    default="source-python/gungame/default/smb3_powerdown.mp3",
)
