#!/usr/bin/env python3

import itertools
import math
import os
import time
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from computer import IntCode

def up():
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()

TILES = {
    0: ' ',
    1: '|',
    2: '#',
    3: '_',
    4: 'O'
}

SIZE = (42, 23)

if __name__ == "__main__":
    ops = parse_list()
    ops[0] = 2 # play for free
    computer = IntCode(ops)
    screen = [[' ' for _ in range(SIZE[0])] for _ in range(SIZE[1])]
    score = 0
    ball_pos = (0,0)
    paddle_pos = (0,0)
    init_iters = SIZE[0] * SIZE[1]
    i = 0
    joystick_command = 0
    while not computer.is_done():
        try:
            x,y,tile = computer.run(joystick_command)
        except:
            break
        if (x,y) == (-1, 0):
            score = tile
        else:
            screen[y][x] = TILES.get(tile)

            if tile == 3: # set paddle pos
                paddle_pos = (x, y)
            if tile == 4:
                ball_pos = (x, y)
            
            if paddle_pos[0] < ball_pos[0]:
                joystick_command = 1
            elif paddle_pos[0] > ball_pos[0]:
                joystick_command = -1
            else:
                joystick_command = 0
        
        s = f'Score: {score}\n'
        s += '\n'.join([''.join(line) for line in screen])
        print(s, flush=True)
        for _ in range(SIZE[1] + 1):
            up()
        if i < init_iters:
            i += 1
        else:
            time.sleep(0.025)
        
    s = f'Score: {score}\n'
    s += '\n'.join([''.join(line) for line in screen])
