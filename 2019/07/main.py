#!/usr/bin/env python3

import itertools
import math
import os
import time
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from computer import IntCode


if __name__ == "__main__":
    ops = parse_list()

    signals = []
    mx = 0
    mx_phase = None
    assert len(list(itertools.permutations(range(5, 10), 5))) == 5 * 4 * 3 * 2
    for phase in itertools.permutations(range(5, 10), 5):
        computers = [IntCode(ops), IntCode(ops), IntCode(ops), IntCode(ops), IntCode(ops)]

        x = 0

        for i, c in enumerate(computers):
            x = c.input = [phase[i], x]
            x = c.run()
        
        while all(not c.is_done() for c in computers):
            for c in computers:
                c.input = [x]
                x = c.run()
                # if not c.is_done():
                #     x = a

        if x > mx:
            mx = x
            mx_phase = phase
        
    print(mx, mx_phase)



