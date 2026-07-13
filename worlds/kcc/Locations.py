# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import CanvasCurseWorld

# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "CanvasCurseWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in locationTable:
        # If we did not turn on extra locations (see how readable it is with that thing from the top)
        # AND the name of it is found in our extra locations table, then that means we dont want to count it
        # So continue moves onto the next name in the table
        # If the location is valid though, count it
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in locationTable.items()}

    return names

# The check to make sure the location is valid
# I know it looks like the same as when we counted it but thats because this is an example
# Things get complicated fast so having a back up is nice
def is_valid_location(world: "CanvasCurseWorld", name) -> bool:
    
    return True

# You might need more functions as well so be liberal with them
# My advice, if you are about to type the same thing in a second time, turn it into a function
# Even if you only do it once you can turn it into a function too for organization

# Heres where you do the next fun part of listing out all those locations
# Its a lot
# My advice, zone out for half an hour listening to music and hope you wake up to a completed list
MainStoryLocations = {
    # You can take a peak at Types.py for more information but,
    # LocData is code, region in this instance
    # Regions will be explained more in Regions.py
    # But just know that it's mostly about organization
    # Place locations together based on where they are in the game and what is needed to get there

    "Plant Plain - Medal 1": LocData(1, "Plant Plain"),
    "Plant Plain - Medal 2": LocData(2, "Plant Plain"),
    "Plant Plain - Medal 3": LocData(3, "Plant Plain"),

    "Tiny Town - Medal 1": LocData(4, "Tiny Town"),
    "Tiny Town - Medal 2": LocData(5, "Tiny Town"),
    "Tiny Town - Medal 3": LocData(6, "Tiny Town"),

    "Ravine Road - Medal 1": LocData(7, "Ravine Road"),
    "Ravine Road - Medal 2": LocData(8, "Ravine Road"),
    "Ravine Road - Medal 3": LocData(9, "Ravine Road"),

    "Ghost Grounds - Medal 1": LocData(10, "Ghost Grounds"),
    "Ghost Grounds - Medal 2": LocData(11, "Ghost Grounds"),
    "Ghost Grounds - Medal 3": LocData(12, "Ghost Grounds"),

    "Growth Grasses - Medal 1": LocData(13, "Growth Grasses"),
    "Growth Grasses - Medal 2": LocData(14, "Growth Grasses"),
    "Growth Grasses - Medal 3": LocData(15, "Growth Grasses"),

    "Mag Mount - Medal 1": LocData(16, "Mag Mount"),
    "Mag Mount - Medal 2": LocData(17, "Mag Mount"),
    "Mag Mount - Medal 3": LocData(18, "Mag Mount"),

    "Rift Ruin - Medal 1": LocData(19, "Rift Ruin"),
    "Rift Ruin - Medal 2": LocData(20, "Rift Ruin"),
    "Rift Ruin - Medal 3": LocData(21, "Rift Ruin"),

    "Contrast Cave - Medal 1": LocData(22, "Contrast Cave"),
    "Contrast Cave - Medal 2": LocData(23, "Contrast Cave"),
    "Contrast Cave - Medal 3": LocData(24, "Contrast Cave"),

    "Silver Submarine - Medal 1": LocData(25, "Silver Submarine"),
    "Silver Submarine - Medal 2": LocData(26, "Silver Submarine"),
    "Silver Submarine - Medal 3": LocData(27, "Silver Submarine"),

    "Machine Mansion - Medal 1": LocData(28, "Machine Mansion"),
    "Machine Mansion - Medal 2": LocData(29, "Machine Mansion"),
    "Machine Mansion - Medal 3": LocData(30, "Machine Mansion"),

    "Dreamy Darkness - Medal 1": LocData(31, "Dreamy Darkness"),
    "Dreamy Darkness - Medal 2": LocData(32, "Dreamy Darkness"),
    "Dreamy Darkness - Medal 3": LocData(33, "Dreamy Darkness"),

    "Paletto Polis - Medal 1": LocData(34, "Paletto Polis"),
    "Paletto Polis - Medal 2": LocData(35, "Paletto Polis"),
    "Paletto Polis - Medal 3": LocData(36, "Paletto Polis"),

    "Cold Course - Medal 1": LocData(37, "Cold Course"),
    "Cold Course - Medal 2": LocData(38, "Cold Course"),
    "Cold Course - Medal 3": LocData(39, "Cold Course"),

    "Dungeon Dome - Medal 1": LocData(40, "Dungeon Dome"),
    "Dungeon Dome - Medal 2": LocData(41, "Dungeon Dome"),
    "Dungeon Dome - Medal 3": LocData(42, "Dungeon Dome"),

    "Canvas Canyon - Medal 1": LocData(43, "Canvas Canyon"),
    "Canvas Canyon - Medal 2": LocData(44, "Canvas Canyon"),
    "Canvas Canyon - Medal 3": LocData(45, "Canvas Canyon"),

    "Collapse Castle - Medal 1": LocData(46, "Collapse Castle"),
    "Collapse Castle - Medal 2": LocData(47, "Collapse Castle"),
    "Collapse Castle - Medal 3": LocData(48, "Collapse Castle"),

    "Volatile Volcano - Medal 1": LocData(49, "Volatile Volcano"),
    "Volatile Volcano - Medal 2": LocData(50, "Volatile Volcano"),
    "Volatile Volcano - Medal 3": LocData(51, "Volatile Volcano"),

    "Silent Seabed - Medal 1": LocData(52, "Silent Seabed"),
    "Silent Seabed - Medal 2": LocData(53, "Silent Seabed"),
    "Silent Seabed - Medal 3": LocData(54, "Silent Seabed"),

    "Frozen Fantasy - Medal 1": LocData(55, "Frozen Fantasy"),
    "Frozen Fantasy - Medal 2": LocData(56, "Frozen Fantasy"),
    "Frozen Fantasy - Medal 3": LocData(57, "Frozen Fantasy"),

    "Mad Mechanism - Medal 1": LocData(58, "Mad Mechanism"),
    "Mad Mechanism - Medal 2": LocData(59, "Mad Mechanism"),
    "Mad Mechanism - Medal 3": LocData(60, "Mad Mechanism"),

    "Spectacle Space - Medal 1": LocData(61, "Spectacle Space"),
    "Spectacle Space - Medal 2": LocData(62, "Spectacle Space"),
    "Spectacle Space - Medal 3": LocData(63, "Spectacle Space"),

    "The World of Drawcia - Medal 1": LocData(64, "The World of Drawcia"),
    "The World of Drawcia - Medal 2": LocData(65, "The World of Drawcia"),
}



# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
locationTable = {
    **MainStoryLocations,
}