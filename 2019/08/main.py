#!/usr/bin/env python3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


if __name__ == "__main__":
    string = parse_as_str().strip()

    WIDTH, HEIGHT = 25, 6

    i = 0
    layers = []
    while i < len(string):
        layers.append(string[i: i + HEIGHT * WIDTH])
        i += WIDTH * HEIGHT

    # Part 1
    layer = sorted(layers, key=lambda layer: layer.count('0'))[0]
    print(layer.count('1') * layer.count('2'))

    # Part 2
    for i in range(WIDTH * HEIGHT):
        if i % WIDTH == 0:
            sys.stdout.write('\n')

        c, j= layers[0][i], 1
        while c == '2':
            c = layers[j][i]
            j += 1
        sys.stdout.write('#' if c == '1' else ' ')

