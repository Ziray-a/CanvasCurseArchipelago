from BaseClasses import Region
from .Types import APSkeletonLocation
from .Locations import locationTable, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CanvasCurseWorld

# This is where you will create your imaginary game world
# IE: connect rooms and areas together
# This is NOT where you'll add requirements for how to get to certain locations thats in Rules.py
# This is also long and tediouos
def createRegions(world: "CanvasCurseWorld"):
    # The functions that are being used here will be located at the bottom to view
    # The important part is that if its not a dead end and connects to another place then name it
    # Otherwise you can just create the connection. Not that naming it is bad

    # You can technically name your connections whatever you want as well
    # You'll use those connection names in Rules.py
    world1 = createRegion(world,"Reddy Land - Kirby")
    world2 = createRegion(world,"Arange Gorge - Kirby")
    world3 = createRegion(world,"Iello Adventure - Kirby")
    world4 = createRegion(world,"Neo Greo - Kirby")
    world5 = createRegion(world,"Bloo Hills - Kirby")
    world6 = createRegion(world,"Omarine Zone - Kirby")
    world7 = createRegion(world,"Wonder Lilane - Kirby")
    world8 = createRegion(world,"The World of Drawcia - Kirby")

    PlantPlain = createRegionAndConnect(world,"Plant Plain", world1)
    TinyTown = createRegionAndConnect(world,"Tiny Town", world1)
    RavineRoad = createRegionAndConnect(world,"Ravine Road")


    GhostGrounds = createRegionAndConnect(world, "Ghost Grounds", world2)
    GrowthGrasses = createRegionAndConnect(world, "Growth Grasses", world2)
    MagMount = createRegionAndConnect(world, "Mag Mount", world2)

    RiftRuin = createRegionAndConnect(world, "Rift Ruin", world3)
    ContrastCave = createRegionAndConnect(world, "Contrast Cave", world3)
    SilverSubmarine = createRegionAndConnect(world, "Silver Submarine", world3)

    MachineMansion = createRegionAndConnect(world, "Machine Mansion", world4)
    DreamyDarkness = createRegionAndConnect(world, "Dreamy Darkness", world4)
    PalettoPolis = createRegionAndConnect(world, "Paletto Polis", world4)

    ColdCourse = createRegionAndConnect(world, "Cold Course", world5)
    DungeonDome = createRegionAndConnect(world, "Dungeon Dome", world5)
    CanvasCanyon = createRegionAndConnect(world, "Canvas Canyon", world5)

    CollapseCastle = createRegionAndConnect(world, "Collapse Castle", world6)
    VolatileVolcano = createRegionAndConnect(world, "Volatile Volcano", world6)
    SilentSeabed = createRegionAndConnect(world, "Silent Seabed", world6)

    FrozenFantasy = createRegionAndConnect(world, "Frozen Fantasy", world7)
    MadMechanism = createRegionAndConnect(world, "Mad Mechanism", world7)
    SpectacleSpace = createRegionAndConnect(world, "Spectacle Space", world7)

    TheWorldOfDrawcia = createRegionAndConnect(world, "The World of Drawcia", world8)


def createRegion(world: "CanvasCurseWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in locationTable.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = APSkeletonLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

# This runs the create region function while also connecting to another region
# Just simplifies process since you woill be connecting a lot of regions
def createRegionAndConnect(world: "CanvasCurseWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = createRegion(world, name)
    connected_region.connect(reg, entrancename)
    return reg