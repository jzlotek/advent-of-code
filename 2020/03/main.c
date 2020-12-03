#include "aoc.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long numtrees(INT_ARRAY trees, int right, int down, int width, int height) {
  long num = 0;
  int r = 0, c = 0;

  while (r < height) {
    num += arr_get(trees, r * width + c) == '#';
    r += down;
    c += right;
    c %= width;
  }

  return num;
}

int main() {

  INT_ARRAY trees = parse_arr_chars();

  int height = 323, width = 31;
  int num = numtrees(trees, 3, 1, width, height);
  printf("%d\n", num);

  unsigned long prod =
    numtrees(trees, 1, 1, width, height) *
    numtrees(trees, 3, 1, width, height) *
    numtrees(trees, 5, 1, width, height) *
    numtrees(trees, 7, 1, width, height) *
    numtrees(trees, 1, 2, width, height);
  printf("%lu\n", prod);

  clean_int_array(trees);

  return 0;
}
