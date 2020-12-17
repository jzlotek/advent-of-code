#!/usr/bin/env python3

import itertools
import math
import os
import sys
import copy
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from util.printing import print_grid

ACTIVE = '#'
INACTIVE = '.'

def get_next(x, y, z, w, grid):
    curr = grid.get((x,y,z,w), INACTIVE)
    count = 0
    for (a,b,c,d) in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2), range(-1,2)):
        count += (1 if grid.get((x+a,y+b,z+c,w+d), INACTIVE) == ACTIVE else 0)

    if curr == ACTIVE:
        return ACTIVE if count == 4 or count == 3 else INACTIVE
    else:
        return ACTIVE if count == 3 else INACTIVE


def iterate(state):
    next_state = copy.deepcopy(state)

    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    zs = [c[2] for c in grid.keys()]
    ws = [c[3] for c in grid.keys()]
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            for z in range(min(zs) - 1, max(zs) + 2):
                for w in range(min(ws) - 1, max(ws) + 2):
                    next_state[(x,y,z,w)] = get_next(x, y, z, w,  state)

    return next_state


if __name__ == "__main__":
    grid = {}
    input_val = parse_as_str_list()

    for i, line in enumerate(input_val):
        for j, c in enumerate(line):
            grid[(i,j,0,0)] = c

    for _ in range(6):
        grid = iterate(grid)

    print(len([x for x in grid.values() if x == ACTIVE]))


