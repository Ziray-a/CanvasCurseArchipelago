# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .Types import ItemData, CanvasCurseItem
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import CanvasCurseWorld

# If you're curious about the -> List[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself
def createItemPool(world: "CanvasCurseWorld") -> List[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    itempool: List[Item] = []
    # In this function is where you would remove any starting items that you add in options such as starting chapter
    # This is also the place you would add dynamic amounts of items from options
    # I can point to Sly Cooper and the Thievious Raccoonus since I did that

    # This is a good place to grab anything you need from options
    
    
    # It's up to you and how you want things organized but I like to deal with victory here
    # This creates your win item and then places it at the "location" where you win
    itempool += getMainItems(world)

    # Then junk items are made
    # Check out the create_junk_items function for more details

    return itempool

# This is a generic function to create a singular item
def create_item(world: "CanvasCurseWorld", name: str, ItemType: ItemClassification = ItemClassification.progression) -> Item:
    data = item_table[name]
    return CanvasCurseItem(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
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



# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers dont trust them PLEASE
# I've seen some games that dynamically add item codes such as DOOM as well
MainItems = {
    # Progression items
    "Progressive World Unlock": ItemData(1001,ItemClassification.progression, 7),
    "Medal": ItemData(1002,ItemClassification.useful,250)

}


# In the way that I made items, I added a way to specify how many of an item should exist
# That's why junk has a 0 since how many are created is in the create_junk_items
# There is a better way of doing this but this is my jank

# This makes a really convenient list of all the other dictionaries
# (fun fact: {} is a dictionary)
item_table = {
    **MainItems
}