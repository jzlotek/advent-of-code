#!/usr/bin/env python3

import itertools
import math
import os
import sys
import re
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


def part1(color, bags):
    ret = set()
    if color in bags:
        for _, c in bags[color]:
            ret.add(c)
            ret.update(part1(c, bags))
    return ret

def part2(color, bags):
    return sum([n + n * part2(c, bags) for n, c in bags[color]])



if __name__ == "__main__":
    lines = parse_as_str_list()
    bags = {}

    for line in lines:
        a, b = re.match(r'^(.+?) bags contain (.+)\.$', line).groups()
        b = [re.match(r'(\d+) (.+) bags?', c).groups() for c in b.split(', ') if c != 'no other bags']
        b = [(int(num), color) for num, color in b]
        bags[a] = b

    print(sum(['shiny gold' in part1(c, bags) for c in bags.keys()]))
    print(part2('shiny gold', bags))




