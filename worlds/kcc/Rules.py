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

    # Chapter Access
    add_rule(world.multiworld.get_entrance("Menu -> Green Hill Zone", player),
             lambda state: state.has("Green Hill Zone", player))

    
    
    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Beat Drawcia", player)