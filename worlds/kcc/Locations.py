from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import CanvasCurseWorld


def get_total_locations(world: "CanvasCurseWorld") -> int:

    total = 0
    for name in locationTable:


        if is_valid_location(world, name):
            total += 1

    return total


def get_location_names() -> Dict[str, int]:

    names = {name: data.ap_code for name, data in locationTable.items()}

    return names



#Returns true for now, since there is no conditional locations yet
def is_valid_location(world: "CanvasCurseWorld", name) -> bool:
    
    return True


# Main story locations (Medals only for now, might need to segment this further)
MainStoryLocations = {

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


locationTable = {
    **MainStoryLocations,
}