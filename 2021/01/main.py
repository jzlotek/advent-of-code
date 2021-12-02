#!/usr/bin/env python3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


if __name__ == "__main__":
    nums = parse_list()
    print(len(list(filter(lambda x: x[0] != 0 and nums[x[0]-1] < x[1], enumerate(nums)))))
    print(len(list(filter(lambda idx: sum(nums[idx-2: idx+1]) < sum(nums[idx-1:idx+2]), range(2, len(nums)-1)))))

