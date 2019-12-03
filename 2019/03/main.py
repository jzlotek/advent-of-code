#!/usr/bin/env python3

# Advent of Code
# Day 3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

def create_wire(direction, curr_pos):
    dirs = {'U': (0,-1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    d = dirs.get(direction)
    return tuple(map(sum, zip(d, curr_pos)))


if __name__ == "__main__":
    wires = parse_list2d(data_type=str)

    points = []
    for wire in wires:
        wire_pts = {}
        pos = (0,0)
        counter = 0
        for ins in wire:
            for _ in range(int(ins[1:])):
                counter += 1
                pos = create_wire(ins[0], pos)
                if pos not in wire_pts:
                    wire_pts[pos] = counter
        points.append(wire_pts)


    intersections = points[0].keys() & points[1].keys()
    # part 1
    print(min(abs(x) + abs(y) for x,y in intersections))
    # part 2
    print(min(abs(points[0][point]) + abs(points[1][point]) for point in intersections))

