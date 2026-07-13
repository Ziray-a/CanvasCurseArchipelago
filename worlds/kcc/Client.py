import logging
from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


class KirbyCanvasCurseClient(BizHawkClient):
    logger = logging.getLogger("Client")
    game = "Kirby: Canvas Curse DS"
    system = "NDS"
    patch_suffix = ".apkcc"
    ram_mem_domain = "Main RAM"

    STAGE_DATA_OFFSET = 0x2D8

    def __init__(self) -> None:
        super().__init__()
        self.rom_slot_name = None
        self.seed_verify = False





    def get_ap_location_id(self, stage_idx, medal_idx):
        return (stage_idx * 3) + medal_idx + 1

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x0, 11, "ROM")]))[0]).decode("ascii")
            if rom_name != "TOUCH!KIRBY":
                return False  
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        ctx.game = self.game
        ctx.items_handling = 0b011
        ctx.want_slot_data = True
        self.rom_slot_name = rom_name
        ctx.watcher_timeout = 0.5

        return True


#there is an off-by-one issue im to lazy to fix
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            save_block_start = 0x0DA300
            save_data = (await bizhawk.read(
                ctx.bizhawk_ctx,
                [(save_block_start, 0x336, self.ram_mem_domain)]
            ))[0]


            currentslot = int.from_bytes((await bizhawk.read(
                ctx.bizhawk_ctx,
                [(0xDA528,1,self.ram_mem_domain)]
            ))[0])

            #skip if not in a slot
            if currentslot != 255:
                #Handle Level Progression
                ap_level_unlocks: int = len([item for item in ctx.items_received if item.item == 1001])
                await bizhawk.write(
                    ctx.bizhawk_ctx,
                    [(save_block_start+0x28, int.to_bytes(ap_level_unlocks,4, "little"),self.ram_mem_domain)])

                # Handle Medal collection
                locations_to_send = []

                for stage_idx in range(21):
                    stage_byte = save_data[self.STAGE_DATA_OFFSET + stage_idx]
                    
                    # Bit 0 (0x01) = Medal 1
                    if stage_byte & 0x01:
                        locations_to_send.append(self.get_ap_location_id(stage_idx, 0))
                    # Bit 1 (0x02) = Medal 2
                    if stage_byte & 0x02:
                        locations_to_send.append(self.get_ap_location_id(stage_idx, 1))
                    # Bit 2 (0x04) = Medal 3
                    if stage_byte & 0x04:
                        locations_to_send.append(self.get_ap_location_id(stage_idx, 2))

                # Handle Stage 8-1 (Drawcia) separately since it only has 2 medals
                drawcia_byte = save_data[self.STAGE_DATA_OFFSET + 21]  # 21 is the 22nd byte
                if drawcia_byte & 0x01:
                    locations_to_send.append(self.get_ap_location_id(21, 0))
                if drawcia_byte & 0x02:
                    locations_to_send.append(self.get_ap_location_id(21, 1))

                # Send the batch to the server
                # We filter out locations the server already knows we checked to save bandwidth
                missing_locations = [loc for loc in locations_to_send if loc not in ctx.checked_locations]
                
                if missing_locations:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": missing_locations
                    }])



                #Handle Medals
                game_total_medals : int = int.from_bytes(save_data[0x90:0x94], "little")
                game_current_medals : int = int.from_bytes(save_data[0x94:0x98], "little")
                ap_total_medals : int = len([item for item in ctx.items_received if item.item == 1002 ])



                if game_total_medals != ap_total_medals:
                    new_medals : int = ap_total_medals - game_total_medals
                    new_game_current_medals : int = game_current_medals + new_medals 
                    await bizhawk.write(ctx.bizhawk_ctx,
                                        [(save_block_start+0x94,int.to_bytes(new_game_current_medals,4,"little"), self.ram_mem_domain)])
                    await bizhawk.write(ctx.bizhawk_ctx,
                                        [(save_block_start+0x90,int.to_bytes(ap_total_medals,4,"little"), self.ram_mem_domain)])


            # Send game clear
            if not ctx.finished_game and (save_data[0x335] & 0x01):
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])


        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass
