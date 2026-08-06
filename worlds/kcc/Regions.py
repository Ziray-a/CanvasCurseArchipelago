from BaseClasses import Region
from .Types import CanvasCurseLocation
from .Locations import locationTable, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CanvasCurseWorld


def create_regions(world: "CanvasCurseWorld"):


    menu = createRegion(world, "Menu")
    world1 = createRegionAndConnect(world,"Reddy Land - Kirby","Menu Select",menu)
    world2 = createRegionAndConnect(world,"Arange Gorge - Kirby","World 2", world1)
    world3 = createRegionAndConnect(world,"Iello Adventure - Kirby","World 3",world2)
    world4 = createRegionAndConnect(world,"Neo Greo - Kirby","World 4",world3)
    world5 = createRegionAndConnect(world,"Bloo Hills - Kirby","World 5",world4)
    world6 = createRegionAndConnect(world,"Omarine Zone - Kirby","World 6",world5)
    world7 = createRegionAndConnect(world,"Wonder Lilane - Kirby","World 7",world6)
    world8 = createRegionAndConnect(world,"The World of Drawcia - Kirby","World 8",world7)

    #Using Variables in case those Regions are going to be used in the future

    PlantPlain = createRegionAndConnect(world,"Plant Plain", "World 1 - Stage 1", world1)
    TinyTown = createRegionAndConnect(world,"Tiny Town","World 1 - Stage 2", world1)
    RavineRoad = createRegionAndConnect(world,"Ravine Road","World 1 - Stage 3", world1)


    GhostGrounds = createRegionAndConnect(world, "Ghost Grounds","World 2 - Stage 1", world2)
    GrowthGrasses = createRegionAndConnect(world, "Growth Grasses","World 2  - Stage 2", world2)
    MagMount = createRegionAndConnect(world, "Mag Mount", "World 2 - Stage 3" , world2)

    RiftRuin = createRegionAndConnect(world, "Rift Ruin","World 3 - Stage 1", world3)
    ContrastCave = createRegionAndConnect(world, "Contrast Cave","World 3 - Stage 2", world3)
    SilverSubmarine = createRegionAndConnect(world, "Silver Submarine","World 3 - Stage 3", world3)

    MachineMansion = createRegionAndConnect(world, "Machine Mansion","World 4 - Stage 1", world4)
    DreamyDarkness = createRegionAndConnect(world, "Dreamy Darkness","World 4 - Stage 2", world4)
    PalettoPolis = createRegionAndConnect(world, "Paletto Polis","World 4 - Stage 3", world4)

    ColdCourse = createRegionAndConnect(world, "Cold Course","World 5 - Stage 1", world5)
    DungeonDome = createRegionAndConnect(world, "Dungeon Dome","World 5 - Stage 2", world5)
    CanvasCanyon = createRegionAndConnect(world, "Canvas Canyon","World 5 - Stage 3", world5)

    CollapseCastle = createRegionAndConnect(world, "Collapse Castle","World 6 - Stage 1", world6)
    VolatileVolcano = createRegionAndConnect(world, "Volatile Volcano","World 6 - Stage 2", world6)
    SilentSeabed = createRegionAndConnect(world, "Silent Seabed","World 6 - Stage 3", world6)

    FrozenFantasy = createRegionAndConnect(world, "Frozen Fantasy","World 7 - Stage 1", world7)
    MadMechanism = createRegionAndConnect(world, "Mad Mechanism","World 7 - Stage 2", world7)
    SpectacleSpace = createRegionAndConnect(world, "Spectacle Space","World 7 - Stage 3", world7)

    TheWorldOfDrawcia = createRegionAndConnect(world, "The World of Drawcia","World 8 - Stage 1", world8)


def createRegion(world: "CanvasCurseWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)


    for (key, data) in locationTable.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = CanvasCurseLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg


def createRegionAndConnect(world: "CanvasCurseWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = createRegion(world, name)
    connected_region.connect(reg, entrancename)
    return reg