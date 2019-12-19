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


def print_grid(grid, flush=False):
    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            if (x,y) in grid:
                sys.stdout.write(grid[(x,y)])
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    if flush:
        sys.stdout.flush()
        for y in range(min(ys), max(ys) + 2):
            up()


ops = parse_list()
def check(x, y):
    computer = IntCode(ops)
    computer.input = [x,y]
    c = computer.run()
    return c 

if __name__ == "__main__":
    grid = {}
    count = 0
    for (x,y) in itertools.product(range(50), range(50)):
        c = check(x, y)
        grid[(x,y)] = '.' if c == 0 else '#'
        count += c
    print(count)
    print_grid(grid)
    
    x = 0
    for y in range(100, 10000):
        while check(x,y) == 0:
            x += 1
        if check(x + 99, y - 99) == 1:
            print(x * 10000 + (y - 99))
            break
