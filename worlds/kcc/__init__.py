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


class KirbyCanvasCurseWeb(WebWorld):
    
    
    # You shouldnt have to change much here except the name at the bottom!
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

    # There are other built in variables for AP. You can look at other worlds to see your options
    # Like PLEASE look at the various worlds. Its so helpful. Find one you like and you can duplicate a bunch of it

    # This is where you put stuff that need to be done RIGHT away. Typically you can just leave it alone but it can be useful to pop some things here as needed
    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

  

    # Regions are the different locations in your world. So like Undead Burgh in dark souls or Pacifilog Town in pokemon
    # They dont have to match your game, they can be whatever you need them to be for organization
    def create_regions(self):
        # This function comes from your Regions.py and dont worry that it matches the function that its in
        create_regions(self)

        # You can also use this space to do other location creation activities
        # Like if an option is enabled to add extra locations
        # Or the opposite, whatever it is. Just be careful that you arent duplicating locations

    # These are some examples of creating items. The create_itempool(self) function is coming from Items.py in this instance
    # The important part is that the items get into the self.multiworld.itempool as a list of Items
    # Ill try to explain better in the Items.py file 
    def create_items(self):
        self.multiworld.itempool += createItemPool(self)

    # This is just a helper function for turning names into Items. You could do some other stuff here as well
    # ahit does similar if you want another look and bomb rush cyberfunk does it in a slightly different way by turning it into a specific item for that game
    # Again hopefully I do a better job of explaining the Items.py file
    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    # The slot data is what youre sending to the AP server kinda. You dont have to add all your options. Really you want the ones you think a pop tracker would use
    # Seed, Slot, and TotalLocations are all super important for AP though, you need those
    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        return slot_data
    

    def generate_output(self, output_directory: str) -> None:
        try:
            file_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.apkcc")
            patch = TinyPatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            write_tokens(patch)
            patch.write(file_path)
        except Exception:
            raise
    
    # These are used by AP to add and remove items from the player. You can probably just leave them alone
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)

