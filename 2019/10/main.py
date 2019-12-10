#!/usr/bin/env python3

import copy
import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

def gcd(x,y):
    div = math.gcd(x,y)
    return (x // div, y // div)

def get_num_seen(x,y,field):
    if field[y][x] != '#':
        return 0
    init_pos = (x,y)
    maxx, maxy = len(field[0]), len(field)
    seen = 0
    angles = set()

    for i in range(-maxx, maxx + 1):
        for j in range(-maxy, maxy + 1):
            if i == j and i == 0:
                continue
            angle = gcd(i, j)
            pos = copy.deepcopy(init_pos)
            if angle not in angles:
                angles.add(angle)
                pos = (pos[0] + angle[0], pos[1] + angle[1])

                while pos[0] < maxx and pos[1] < maxy and pos[0] >= 0 and pos[1] >= 0:
                    if field[pos[1]][pos[0]] == '#':
                        seen += 1
                        break
                    pos = (pos[0] + angle[0], pos[1] + angle[1])
    return seen

def conv(pos):
    x,y=pos
    return (math.atan2(y,x) + 2 * math.pi - 3 * math.pi / 2) % (2 * math.pi)

def run_laser(init_pos, field):
    maxx, maxy = len(field[0]), len(field)
    angles = set()

    for i in range(-maxx, maxx + 1):
        for j in range(-maxy, maxy + 1):
            if i == j and i == 0:
                continue
            angle = gcd(i, j)
            if angle not in angles:
                angles.add(angle)
    field[init_pos[1]][init_pos[0]] = '@'
    index = 0
    destroyed = 0
    angles = sorted(list(angles), key=lambda x: conv(x))
    while destroyed < 200:
        angle = angles[index % len(angles)]
        pos = (init_pos[0] + angle[0], init_pos[1] + angle[1])

        while pos[0] < maxx and pos[1] < maxy and pos[0] >= 0 and pos[1] >= 0:
            if field[pos[1]][pos[0]] == '#':
                if destroyed == 199:
                    destroyed += 1
                    field[pos[1]][pos[0]] = str(destroyed)
                    print('\n'.join(['\t'.join(line) for line in field]))
                    return pos
                destroyed += 1
                field[pos[1]][pos[0]] = str(destroyed)
                break
            pos = (pos[0] + angle[0], pos[1] + angle[1])
        index += 1

    return pos






if __name__ == "__main__":
    field = parse_as_str_list()
    field = [[c for c in line] for line in field]
    most_seen = 0
    pos = None

    for y in range(len(field)):
        for x in range(len(field[0])):
            seen = get_num_seen(x,y,field)

            if seen > most_seen:
                pos = (x,y)
                most_seen = seen
    print(pos, most_seen)
    pos = run_laser(pos, field)
    print(pos[0] * 100 + pos[1])

