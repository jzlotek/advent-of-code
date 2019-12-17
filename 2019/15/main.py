#!/usr/bin/env python3

import itertools
import math
import os
import time
import sys
import random
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from computer import IntCode

def up():
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()

WALL = '#'
DROID = 'D'
EMPTY = '.'
OXY = '0'

DIRS = {
    1: (0, -1), # "NORTH",
    2: (0, 1), # "SOUTH",
    3: (1, 0), # "EAST",
    4: (-1, 0) # "WEST"
}

def get_char(code):
    if code == 0:
        return WALL
    elif code == 1:
        return EMPTY
    elif code == 2:
        return OXY
    else:
        return ' '

def get_next_pos(curr_pos, direc):
    return tuple(map(sum, zip(curr_pos, DIRS.get(direc))))


def find_next_dir(curr_dir, curr_pos, grid):
    for x in [i for i in range(1, 5) if i != curr_dir]:
        if get_next_pos(curr_pos, x) not in grid:
            return x

    return None

def get_opposite_move(move):
    if move == 1:
        return 2
    elif move == 2:
        return 1
    elif move == 3:
        return 4
    else:
        return 3

def bfs(computer, curr_dir, curr_pos, grid):
    next_pos = get_next_pos(curr_pos, curr_dir)
    if next_pos in grid.keys():
        # print(grid[next_pos])
        return 0
    next_code = computer.run(curr_dir)
    if next_pos not in grid:
        grid[next_pos] = {'tile': get_char(next_code), 'dist': grid[curr_pos].get('dist') + 1}
    print_grid(grid, curr_pos)

    if next_code == 1:
        curr_pos = next_pos
        moves = range(1,5)
        for move in moves:
            if get_next_pos(curr_pos, move) not in grid:
                bfs(computer, move, curr_pos, grid)
        computer.run(get_opposite_move(curr_dir))
    else:
        moves = range(1,5)
        for move in moves:
            if get_next_pos(curr_pos, move) not in grid:
                bfs(computer, move, curr_pos, grid)

def fill_bfs(curr_pos, direction, seen):
    if curr_pos in seen:
        return 0
    else:
        seen.add(curr_pos)
    if grid[curr_pos].get('tile') in [WALL]:
        return 0
    return max([fill_bfs(get_next_pos(curr_pos, move), move, seen) + 1 for move in range(1,5) if move != get_opposite_move(direction)])
    


def print_grid(grid, curr_pos):
    # time.sleep(0.025)
    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            if (x, y) == (0,0):
                sys.stdout.write('@')
            elif (x, y) == curr_pos:
                sys.stdout.write('D')
            elif (x,y) in grid:
                sys.stdout.write(grid[(x,y)].get('tile'))
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    sys.stdout.flush()
    for y in range(min(ys), max(ys) + 2):
        up()



if __name__ == "__main__":
    ops = parse_list()
    computer = IntCode(ops)

    curr_dir = 1
    moves = []
    grid = {}
    curr_pos = (0,0)
    grid[curr_pos] = {'tile': EMPTY, 'dist': 0}


    bfs(computer, curr_dir, curr_pos, grid)
    print_grid(grid, curr_pos)
    oxys = filter(lambda x: x[1].get('tile') == OXY, grid.items())
    min_dist = sorted(oxys, key=lambda x: x[1].get('dist'))[0]
    print(min_dist[1].get('dist'))

    curr_pos = min_dist[0]
    print(max([fill_bfs(curr_pos, move, set()) for move in range(1, 5)]) - 1)
