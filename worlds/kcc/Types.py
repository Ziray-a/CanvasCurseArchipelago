from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification


class CanvasCurseLocation(Location):
    game = "Kirby: Canvas Curse DS"

class CanvasCurseItem(Item):
    game = "Kirby: Canvas Curse DS"


class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1


class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
