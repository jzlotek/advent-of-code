#!/usr/bin/env python3

import itertools
import math
import os
import sys
from math import prod
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

def inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def findMinX(num, rem):
    result = 0
    p = prod(num)
    for n, r in zip(num, rem):
        pp = p // n
        result += r * inv(pp, n) * pp
    return result % p

def sol(busses):
    rems = list(map(lambda x: -x[0] % x[1], busses))
    nums = list(map(lambda x: x[1], busses))
    return findMinX(nums, rems)

if __name__ == "__main__":
    lines = parse_as_str_list()
    timestamp = int(lines[0])
    busses = list(map(int, [x for x in lines[1].split(',') if x != 'x']))

    t = min(map(lambda x: ((timestamp // x + 1) * x, x), busses))
    print((t[0] - timestamp) * t[1])

    lines = parse_as_str_list()
    busses = [(idx, int(x)) for idx, x in enumerate(lines[1].split(',')) if x != 'x']
    print(sol(busses))


