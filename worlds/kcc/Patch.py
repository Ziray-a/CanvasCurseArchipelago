#Small Patch file, the smallest I could think of to make it work with the patcher from AP
import os

from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import CanvasCurseWorld



class TinyPatch(APProcedurePatch, APTokenMixin):
    game = "Kirby: Canvas Curse DS"
    hash = "1bf9f30c507a12dda0ec0a33daeeed0b"
    patch_file_ending = ".apkcc"
    result_file_ending = ".nds"


    procedure = [
        ("apply_tokens", ["token_data.bin"])
        ]

    @classmethod
    def get_source_data(cls):
        with open(get_settings().kcc_options.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read());
        return base_rom_bytes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def get_manifest(self):
        manifest= super().get_manifest()
        manifest["patch_file_ending"] = self.patch_file_ending
        manifest["game"] = self.game
        return manifest
    


def write_tokens(
    #world: "CanvasCurseWorld",
    patch: TinyPatch
) -> None:
    world_clear_counter_addr = 0x505fe   # 2 bytes 
    patch.write_token(APTokenTypes.WRITE, world_clear_counter_addr, [0x46, 0xc0])
    patch.write_file("token_data.bin", patch.get_token_binary())
    


