from worlds.generic.Rules import add_rule, set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CanvasCurseWorld

def set_rules(world: "CanvasCurseWorld"):

 

    player = world.player
    options = world.options

    
    # World Progression Rules 
    add_rule(world.multiworld.get_entrance("World 2", player),
             lambda state: state.count("Progressive World Unlock", player) >= 1)
    add_rule(world.multiworld.get_entrance("World 3", player),
             lambda state: state.count("Progressive World Unlock", player) >= 2)
    add_rule(world.multiworld.get_entrance("World 4", player),
             lambda state: state.count("Progressive World Unlock", player) >= 3)
    add_rule(world.multiworld.get_entrance("World 5", player),
             lambda state: state.count("Progressive World Unlock", player) >= 4)
    add_rule(world.multiworld.get_entrance("World 6", player),
             lambda state: state.count("Progressive World Unlock", player) >= 5)
    add_rule(world.multiworld.get_entrance("World 7", player),
             lambda state: state.count("Progressive World Unlock", player) >= 6)  
    add_rule(world.multiworld.get_entrance("World 8", player),
             lambda state: state.count("Progressive World Unlock", player) >= 7)
    
    #Orange Button Rules
    add_rule(world.multiworld.get_location("Tiny Town - Medal 2", player),
             lambda state: state.count("Progressive World Unlock", player) >= 2)
    add_rule(world.multiworld.get_location("Ghost Grounds - Medal 3", player),
             lambda state: state.count("Progressive World Unlock", player) >= 2)
    
    #Green Button Rules
    add_rule(world.multiworld.get_location("Contrast Cave - Medal 3", player),
             lambda state: state.count("Progressive World Unlock", player) >= 4) 
    add_rule(world.multiworld.get_location("Paletto Polis - Medal 1", player),
             lambda state: state.count("Progressive World Unlock", player) >= 4)    
   
   #Blue Button Rules
    add_rule(world.multiworld.get_location("Canvas Canyon - Medal 3", player),
             lambda state: state.count("Progressive World Unlock", player) >= 6) 
    add_rule(world.multiworld.get_location("Collapse Castle - Medal 2", player),
             lambda state: state.count("Progressive World Unlock", player) >= 6) 

