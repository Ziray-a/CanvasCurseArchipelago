from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range


def createOptionGroups() -> List[OptionGroup]:
    OptionGroupList: List[OptionGroup] = []
    for name, options in OptionGroups.items():
        OptionGroupList.append(OptionGroup(name=name, options=options))

    return OptionGroupList


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


class IncludeRainbowRun(bool):
    '''
    Includes Medals Locations from the Rainbow Run 
    Medals are already Included, due to the Game needing more than just the Medals from Story mode to get everything inside the Medal Exchange
    '''
    display_name = "Include Rainbow Run"
    default = False

class RainbowRunDifficulty(Range):
    '''
    Determines what Medals are counted as in-logic.
    Use this if you are not confident you can get 3 Medals in every Rainbow Run Challenge 
    '''
    display_name = "Rainbow Run Difficulty"
    range_start = 1
    range_end = 3
    default = 3


class IncludeMedalExchange(bool):
    '''
    WARNING: THIS WILL NOT WORK IF YOU ARE IN SINGLE-PLAYER ARCHIPELAGO SINCE THERE ARE NOT ENOUGH LOCATIONS (yet)
    This Randomizes the Medal exchange Items as well.
    Adds trash such as Songs and Lines Inside the Medal exchange, but adds Checks to the Medal-Shop unlocks
    '''
    display_name = "Include Medal Exchange"
    default= False


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

OptionGroups: Dict[str, List[Any]] = {
    "Trap Options": [TrapChance, LosePowerupTrapWeight, IncludeRainbowRun]
}