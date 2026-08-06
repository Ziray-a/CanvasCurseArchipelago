from enum import IntEnum
from typing import NamedTuple, Optional, Tuple
from BaseClasses import Location, Item, ItemClassification
from Options import OptionGroup


class CanvasCurseLocation(Location):
    game = "Kirby: Canvas Curse DS"

class CanvasCurseItem(Item):
    game = "Kirby: Canvas Curse DS"


class IItemData(NamedTuple):
    ap_code: Optional[int]
    count: Optional[int] = 1

class ItemData(IItemData):
    classification: ItemClassification
    is_option_dependant = False

class ItemDataOptionDependant(IItemData) :
    classification: Tuple[ItemClassification,ItemClassification]
    option_dependency: OptionGroup
    is_option_dependant = True
class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
