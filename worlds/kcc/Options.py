from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

# If youve ever gone to an options page and seen how sometimes options are grouped
# This is that
def createOptionGroups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in ap_skeleton_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list


class TrapChance(Range):
    """
    Determines the chance for any junk item to become a trap.
    Set it to 0 for no traps.
    Range is in fact a range. You can set the limits and its default.
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0


class LosePowerupTrapWeight(Range):
    """
    The weight of the Lose Power-Up Trap in the trap pool.
    This makes you lose your Power-Up and return to normal Ball-Kirby
    Use at your own risk!
    """
    display_name = "Lose Powe-Up Trap Weight"
    range_start = 0
    range_end = 100
    default = 0

class SpeedChangeTrapWeight(Range):
    """
    The weight of speed change traps in the trap pool.
    Speed change traps change the game speed for x seconds.
    """
    display_name = "Speed Change Trap Weight"
    range_start = 0
    range_end = 100
    default = 25

@dataclass
class WorldOptions(PerGameCommonOptions):

    
    TrapChance:                 TrapChance
    SpeedChangeTrapWeight:      SpeedChangeTrapWeight
    LosePowerup: LosePowerupTrapWeight

# This is where you organize your options
# Its entirely up to you how you want to organize it
ap_skeleton_option_groups: Dict[str, List[Any]] = {
    "Trap Options": [TrapChance, SpeedChangeTrapWeight, LosePowerupTrapWeight]
}