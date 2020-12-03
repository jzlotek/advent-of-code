#include "aoc.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numtrees(INT_MATRIX trees, int right, int down) {
  int num = 0;
  int r = 0, c = 0;

  while (r < trees->currheight) {
    num += (char)mat_get(trees, r, c % trees->currwidth) == '#';
    r += down;
    c += right;
  }

  return num;
}

int main() {

  INT_MATRIX trees = parse_mat_chars();

  int num = numtrees(trees, 3, 1);
  printf("%d\n", num);

  unsigned long prod = (long)numtrees(trees, 1, 1) * numtrees(trees, 3, 1) * numtrees(trees, 5, 1) * numtrees(trees, 7, 1) * numtrees(trees, 1, 2);
  printf("%lu\n", prod);

  clean_int_matrix(trees);

  return 0;
}
