#!/usr/bin/env python3

import itertools
import math
import os
import sys
import copy
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


orbits = {}
def get_count(start, depth):
    if start not in orbits.keys():
        return depth
    count = depth

    return count + sum([get_count(child, depth + 1) for child in orbits[start]])


def bfs(start, end):
    seen = set()
    dist = 1
    node = start
    unseen = orbits.get(node, [])
    seen.add(node)

    while len(unseen) > 0:
        next_unseen = []
        for n in unseen:
            if n not in seen:
                if n == end:
                    return dist - 2

                nodes = orbits.get(n, [])
                next_unseen.extend(nodes)
                seen.add(n)

        unseen = next_unseen
        dist += 1


if __name__ == "__main__":
    ob = parse_as_str_list()

    for o in ob:
        a, b = o.split(')')
        l = orbits.get(a, [])
        if l is None:
            l = []
        l.append(b)
        orbits[a] = l
    print(get_count('COM', 0))

    orbits = {}
    # reinit nodes
    for o in ob:
        a, b = o.split(')')
        l = orbits.get(a, [])
        if l is None:
            l = []
        l.append(b)
        orbits[a] = l

        l = orbits.get(b, [])
        if l is None:
            l = []
        l.append(a)
        orbits[b] = l

    print(bfs('YOU', 'SAN'))

