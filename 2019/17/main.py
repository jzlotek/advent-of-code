#!/usr/bin/env python3

import copy
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


DIRS = {
    0: (0, -1), # "NORTH",
    1: (1, 0), # "EAST",
    2: (0, 1), # "SOUTH",
    3: (-1, 0) # "WEST"
}


CHAR_DIRS = {
    '<': 3,
    '>': 1,
    'v': 2,
    '^': 0
}


def opposite(d):
    return (d + 6) % 4


def get_pos(pos, direction):
    return tuple(map(sum, zip(pos, DIRS.get(direction))))


def is_intersection(grid, pos):
    return [grid.get(get_pos(pos, d), None) for d in range(4)].count('#') == 4 and grid[pos] == '#'


def print_grid(grid, flush=False):
    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            if is_intersection(grid, (x,y)):
                sys.stdout.write('O')
            elif (x,y) in grid:
                sys.stdout.write(grid[(x,y)])
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    if flush:
        sys.stdout.flush()
        for y in range(min(ys), max(ys) + 2):
            up()


def get_grid_pathing(grid):
    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    pos = None
    for (x,y) in itertools.product(range(min(xs), max(xs) + 1), range(min(ys), max(ys) + 1)):
        if grid[(x,y)] in ['<', '>', 'v', '^']:
            pos = (x,y)
            break
    curr_dir = CHAR_DIRS[grid[pos]]
    moves = []
    while True:
        next_pos = get_pos(pos, curr_dir)
        num = 0
        while next_pos in grid and grid[next_pos] == '#':
            num += 1
            pos = next_pos
            next_pos = get_pos(pos, curr_dir)
        if num != 0:
            moves.append(str(num))

        last_dir = curr_dir
        for d in [x for x in range(4) if x not in [curr_dir, opposite(curr_dir)]]:
            next_pos = get_pos(pos, d)
            if next_pos in grid and grid[next_pos] == '#':
                if (last_dir + 5) % 4 == d:
                    moves.append('R')
                else:
                    moves.append('L')
                curr_dir = d
                break
        if curr_dir == last_dir:
            break
    moves = ','.join(moves)
    print(moves)


if __name__ == "__main__":
    ops = parse_list()
    computer = IntCode(ops)
    grid = {}
    pos = (0,0)
    while not computer.is_done():
        c = computer.run()
        if c is not None:
            c = chr(c)
        else:
            continue
        if c == '\n':
            pos = (-1, pos[1] + 1)
        else:
            grid[pos] = c
        pos = get_pos(pos, 1)
    print_grid(grid)
    print(sum(map(lambda x: x[0] * x[1], filter(lambda y: is_intersection(grid, y), grid.keys()))))

    # part 2
    get_grid_pathing(grid)

    # reinit computer
    ops = parse_list()
    ops[0] = 2
    computer = IntCode(ops)

    instructions = "A,B,A,C,A,B,C,A,B,C\n"
    A = "R,12,R,4,R,10,R,12\n"
    B = "R,6,L,8,R,10\n"
    C = "L,8,R,4,R,4,R,6\n"
    yn = 'n\n'
    stack = instructions + A + B + C + yn
    computer.input_stack = list(map(ord, stack))

    grid = {}
    pos = (0,0)
    cs = []
    while not computer.is_done():
        c = computer.run()
        cs.append(c)
    print(cs[-1])