import logging


from BaseClasses import Item, ItemClassification


from .Types import ItemData, CanvasCurseItem
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
        if MainItems[MainItem].count >1:
            MainItemPoolList += create_multiple_items(world, MainItem, MainItems[MainItem].count, MainItems[MainItem].classification)
        else:
            MainItemPoolList +=create_item(world, MainItem, MainItems[MainItem].classification)
    return MainItemPoolList



MainItems = {
    # Progression items
    "Progressive World Unlock": ItemData(1001,ItemClassification.progression, 7),
    "Medal": ItemData(1002,ItemClassification.useful,250)

}


item_table = {
    **MainItems
}