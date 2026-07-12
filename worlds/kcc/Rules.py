from worlds.generic.Rules import add_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CanvasCurseWorld

# This is the last big thing to do (at least for me)
# This is where you add item
# These are omega simplified rules
# There are a ton of different ways you can add rules from amoount of items you need to optional items
# Theres also difficulty options and a bunch others
# Id suggest going through a bunch of different ap worlds and seeing how they do the rules
# Even better if its a game you know a lot about and can tell what you need to get to certain locations
def set_rules(world: "CanvasCurseWorld"):
    player = world.player
    options = world.options

    add_rule(world.multiworld.get_entrance("World 2", player),
             lambda state: state.has("Progressive World Unlock", player, 1))
    add_rule(world.multiworld.get_entrance("World 3", player),
             lambda state: state.has("Progressive World Unlock", player, 2))
    add_rule(world.multiworld.get_entrance("World 4", player),
             lambda state: state.has("Progressive World Unlock", player, 3))
    add_rule(world.multiworld.get_entrance("World 5", player),
             lambda state: state.has("Progressive World Unlock", player, 4))
    add_rule(world.multiworld.get_entrance("World 6", player),
             lambda state: state.has("Progressive World Unlock", player, 5))
    add_rule(world.multiworld.get_entrance("World 7", player),
             lambda state: state.has("Progressive World Unlock", player, 6))
    add_rule(world.multiworld.get_entrance("World 8", player),
             lambda state: state.has("Progressive World Unlock", player, 7))
    

