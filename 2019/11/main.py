#!/usr/bin/env python3

import copy
import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d
from computer import IntCode

DIRS = {
  "UP": (0, -1),
  "RIGHT": (1, 0),
  "DOWN": (0, 1),
  "LEFT": (-1, 0),
}

def get_move(curr_dir, turn):
  off = -1 if turn == 0 else 1
  curr_idx = list(DIRS.keys()).index(curr_dir)
  next_t = list(DIRS.keys())[(curr_idx + off + 4) % 4]
  return next_t, DIRS[next_t]

if __name__ == "__main__":
  ops = parse_list()
  computer = IntCode(ops)
  grid = {}
  curr_dir = "UP"
  curr_pos = (0,0)
  # part 2
  grid[curr_pos] = '#'

  while not computer.is_done():
    cell = grid.get(curr_pos, '.')
    curr_color = 1 if cell == '#' else 0
    try:
      paint, move = computer.run(curr_color)
    except TypeError:
      break
    cell = "#" if paint == 1 else '.'
    grid[curr_pos] = cell
    curr_dir, next_dir = get_move(curr_dir, move)
    curr_pos = tuple(map(sum, zip(curr_pos, next_dir)))
  print(len(grid.keys()))

  xs = [c[0] for c in grid.keys()]
  ys = [c[1] for c in grid.keys()]
  for y in range(min(ys), max(ys)+1):
    for x in range(min(xs), max(xs)+1):
      if (x,y) in grid:
        sys.stdout.write('#' if grid[(x,y)] == '#' else ' ')
      else:
        sys.stdout.write(' ')
    sys.stdout.write('\n')
    

