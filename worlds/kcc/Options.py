from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range


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

@dataclass
class WorldOptions(PerGameCommonOptions):

    
    TrapChance:                 TrapChance
    LosePowerup: LosePowerupTrapWeight


ap_skeleton_option_groups: Dict[str, List[Any]] = {
    "Trap Options": [TrapChance, LosePowerupTrapWeight]
}