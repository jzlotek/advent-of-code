#!/usr/bin/env python3

import itertools
import math
import os
import sys
import re
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

def build(rules, rule="0", max_depth=40):
    if max_depth == 0:
        return ""
    if rules[rule][0][0].startswith('"'):
        return rules[rule][0][0].strip('"')
    return f"({'|'.join(''.join([build(rules, r, max_depth-1) for r in subrule]) for subrule in rules[rule])})"

if __name__ == "__main__":
    rules = {}
    lines = iter(parse_as_str_list())
    line = next(lines)
    while line != "":
        d, rest = line.split(":")
        rules[d] = [x.split() for x in rest.split(" | ")]
        line = next(lines)

    # part 2
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

    matches = 0
    reg = re.compile(build(rules))
    for line in lines:
        matches += 1 if reg.fullmatch(line) else 0
    print(matches)



