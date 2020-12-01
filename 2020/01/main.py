#!/usr/bin/env python3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from functools import reduce
from operator import mul


if __name__ == "__main__":
  a = set(parse_list(delim='\n'))
  b = set(2020 - x for x in a)
  res = list(a & b)
  print(res[0] * res[1])

  print(reduce(mul, list(filter(lambda x: sum(x) == 2020, itertools.combinations(list(a), 3)))[0], 1))
