import logging


from BaseClasses import Item, ItemClassification
from worlds.kcc.Options import IncludeRainbowRun

from .Types import ItemData, CanvasCurseItem, ItemDataOptionDependant
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING


if TYPE_CHECKING:
    from . import CanvasCurseWorld


def createItemPool(world: "CanvasCurseWorld") -> List[Item]:

    itempool: List[Item] = []

    
    

    itempool += getMainItems(world)



    return itempool


def create_item(world: "CanvasCurseWorld", name: str, ItemType: ItemClassification = ItemClassification.progression) -> Item:
    data = item_table[name]
    return CanvasCurseItem(name, data.classification, data.ap_code, world.player)


def create_multiple_items(world: "CanvasCurseWorld", name: str, count: int,
                          itemType: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [CanvasCurseItem(name, itemType, data.ap_code, world.player)]

    return itemlist

def getMainItems(world: "CanvasCurseWorld"):
    MainItemPoolList = []
    MainItemKeys = MainItems.keys()
    for MainItem in MainItemKeys:
        if MainItems[MainItem].is_option_dependant:
            if not world.options[MainItems[MainItem].option_dependency]:
                pass
        else: 
            if MainItems[MainItem].count >1:
                MainItemPoolList += create_multiple_items(world, MainItem, MainItems[MainItem].count, MainItems[MainItem].classification)
            else:
                MainItemPoolList += create_item(world, MainItem, MainItems[MainItem].classification)
    return MainItemPoolList


    


MainItems = {
    # Progression items
    "Progressive World Unlock": ItemData(1001,ItemClassification.progression, 7),
    #Medals are more than existing locations, reason being that you can get a total of 250 medals in the game
    #this is supposed to help unlocking health. Be advised that solo archipelagos do not profit from this since there are only 63 locations default
    "Medal": ItemDataOptionDependant(1002, 250, (ItemClassification.progression, ItemClassification.useful), IncludeRainbowRun)

}

MedalExchangeItemsStatic = {
   "Song 1" : ItemData(1101,ItemClassification.filler), 
   "Song 2" : ItemData(1102,ItemClassification.filler),
   "Song 3" : ItemData(1103,ItemClassification.filler),
    "Zebra Line": ItemData(1104, ItemClassification.filler),
    "Bead Line": ItemData(1105, ItemClassification.filler),
    "Tropic Line": ItemData(1106, ItemClassification.filler),
    "Life Boost 1": ItemData(1107, ItemClassification.useful),
    "Life Boost 2": ItemData(1116, ItemClassification.useful),
    "Life Boost 3": ItemData(1117, ItemClassification.useful),
    "Dedede Ball": ItemData(1118, ItemClassification.filler),
    "Meta Knight Ball": ItemData(1119, ItemClassification.filler),
    "Hidden Song": ItemData(1120, ItemClassification.filler), 
}

MedalExchangeItemsRainbowRun = {
    "Course 1": ItemDataOptionDependant(1108, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 2": ItemDataOptionDependant(1109, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun), 
    "Course 3": ItemDataOptionDependant(1110, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 4": ItemDataOptionDependant(1111, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 5 ": ItemDataOptionDependant(1112, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 6 ": ItemDataOptionDependant(1113, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 7 ": ItemDataOptionDependant(1114, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    "Course 8 ": ItemDataOptionDependant(1115, 1, (ItemClassification.progression, ItemClassification.filler) ,IncludeRainbowRun),
    }
    


item_table = {
    **MainItems
}