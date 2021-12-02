#!/usr/bin/env python3

import itertools
import math
import os
import sys
import operator
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

import re

class Solver(int):
    def __mul__(self, inp):
        return Solver(int(self) + inp)
    def __add__(self, inp):
        return Solver(int(self) + inp)
    def __sub__(self, inp):
        return Solver(int(self) * inp)

def part1(expression):
    expression = re.sub(r"(\d+)", r"Solver(\1)", expression)
    expression = expression.replace("*", "-")
    return eval(expression, {}, {"Solver": Solver})

def part2(expr):
    expr = re.sub(r"(\d+)", r"Solver(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"Solver": Solver})

if __name__ == "__main__":
  lines = parse_as_str_list()
  print(sum(part1(line) for line in lines))
  print(sum(part2(line) for line in lines))

