#!/usr/bin/env python3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


def isvalid(num):
    last = str(num)[0]
    has_double = False

    for c in str(num)[1:]:
        if int(last) > int(c):
            return False
        if c == last:
            has_double = True

        last = c

    return has_double


def isvalid2(num):
    last = str(num)[0]
    counts =  {}
    counts[last] = 1

    for c in str(num)[1:]:
        if int(last) > int(c):
            return False
        counts[c] = counts.get(c, 0) + 1

        last = c

    vals = counts.values()
    return 2 in vals


if __name__ == "__main__":
    num = parse_as_str()
    start, stop = list(map(int, num.split('-')))
    nums = []

    for i in range(stop - start + 1):
        if isvalid(start + i):
            nums.append(start+i)

    print(len(nums))

    nums = []

    for i in range(stop - start + 1):
        if isvalid2(start + i):
            nums.append(start+i)
    print(len(nums))





