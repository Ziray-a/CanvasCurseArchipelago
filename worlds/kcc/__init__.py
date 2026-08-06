import os
import typing
import zipfile as zip

from BaseClasses import MultiWorld, Item, Tutorial
import settings
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict
from .Client import KirbyCanvasCurseClient
from .Patch import TinyPatch, write_tokens
from .Locations import get_location_names
from .Items import create_item, createItemPool, item_table
from .Options import WorldOptions
from .Regions import create_regions
from .Rules import set_rules


class KirbyCanvasCurseWeb(WebWorld):
    
    
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up DS Kirby: Canvas Curse for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ziraya)"]
    )]




class KCCSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        copy_to = "Kirby_Canvas_Curse.nds"
        description ="Canvas Curse ROM File"
        md5s = ["1bf9f30c507a12dda0ec0a33daeeed0b"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True


class CanvasCurseWorld(World):
    """
    A game about guiding a now fully ball-shaped Kirby along a rainbow trail.
    """

    game = "Kirby: Canvas Curse DS"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = WorldOptions
    options = WorldOptions
    web = KirbyCanvasCurseWeb()
    settings: typing.ClassVar[KCCSettings]

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

  
    def create_regions(self):
        create_regions(self)


    def create_items(self):
        self.multiworld.itempool += createItemPool(self)


    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        return slot_data
    
    def set_rules(self):
        super().set_rules()
        set_rules(self)

    def generate_output(self, output_directory: str) -> None:
        try:
            file_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.apkcc")
            patch = TinyPatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            write_tokens(patch)
            patch.write(file_path)
        except Exception:
            raise
    

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)
    


