# --- CHANGE THESE ---

minesweeper_us_output = # Paste minesweeper.us output here!
schem_name = 'my_board'


# --- DON'T CHANGE ANYTHING ELSE UNLESS YOU KNOW WHAT YOU'RE DOING ---

import os
import mcschematic

width, height, board = tuple(minesweeper_us_output[:3])
displacement = 9

mine_block = 'minecraft:redstone_block'
safe_block = 'minecraft:redstone_lamp'
lever = 'minecraft:lever[face=ceiling,facing=south]'

schem = mcschematic.MCSchematic()

start_pos = [2, -70, -5]
pos = start_pos.copy()

for y in range(height):
    pos[2] = start_pos[2]

    for x in range(width):
        idx = y * height + x
        num = board[idx]

        if num < 0:
            schem.setBlock(tuple(pos), mine_block)
        else:
            schem.setBlock(tuple(pos), safe_block)

        pos[1] -= 1
        schem.setBlock(tuple(pos), lever)
        pos[1] += 1

        pos[2] -= displacement

    pos[0] += displacement

schem.save(os.path.dirname(os.path.abspath(__file__)), schem_name, mcschematic.Version.JE_1_18_2)

