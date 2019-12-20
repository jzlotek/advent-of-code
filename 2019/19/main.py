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
from util.printing import print_grid
from computer import IntCode

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
