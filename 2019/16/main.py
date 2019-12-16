#!/usr/bin/env python3

import itertools
import math
import os
import time
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

input_list = [int(c) for c in parse_as_str().strip()]

for _ in range(100):
    input_list = [
            abs(sum(x * (0, -1, 0, 1)[(j + 1) % (4 * (i + 1)) // (i + 1)] for j, x in enumerate(input_list))) % 10
            for i in range(len(input_list))
    ]


print(''.join([str(x) for x in input_list[:8]]))
        
input_list = [int(c) for c in parse_as_str().strip()]
offset = int(''.join(map(str, input_list[:7])))
l = len(input_list) * 10000
input_list = [input_list[i % len(input_list)] for i in range(offset, l)]
    
for _ in range(100):
    for i in reversed(range(1, len(input_list))):
        input_list[i - 1] += input_list[i]
    input_list = list(map(lambda x: x % 10, input_list))

print(''.join([str(x) for x in input_list[:8]]))

