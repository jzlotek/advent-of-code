#include "aoc.h"
#include <unistd.h>

const int FLOOR = '.';
const int TAKEN = '#';
const int EMPTY = 'L';

int get_next(INT_MATRIX state, int r, int c) {
  int num_occ = 0;
  int curr = mat_get(state, r, c);
  if (curr == FLOOR)
    return FLOOR;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i == j && i == 0)
        continue;
      if (r + i < 0 || r + i >= height(state))
        continue;
      if (c + j < 0 || c + j >= width(state))
        continue;

      switch(mat_get(state, r + i, c + j)) {
        case '#':
          num_occ++;
          break;
        default: break;
      }
    }
  }

  if (curr == EMPTY && num_occ == 0) return TAKEN;
  if (curr == TAKEN && num_occ >= 4) return EMPTY;
  return curr;
}

void step(INT_MATRIX state, INT_MATRIX dest) {
  for (unsigned int r = 0; r < height(state); r++) {
    for (unsigned int c = 0; c < width(state); c++) {
      mat_set(dest, r, c, get_next(state, r, c));
    }
  }
}

unsigned long count(INT_MATRIX mat) {
  unsigned long count = 0;

  for (unsigned int i = 0; i < height(mat); i++) {
    for (unsigned int j = 0; j < width(mat); j++) {
      count += (int)(mat_get(mat, i, j) == TAKEN);
    }
  }

  return count;
}

void run(INT_MATRIX mat, INT_MATRIX next) {
  INT_MATRIX tmp;

  step(mat, next);

  // HIDE_CURSOR();
  while(!mat_eq(mat, next)) {
    tmp = mat;
    mat = next;
    next = tmp;
    // print_matrix_chars_loop(mat);
    step(mat, next);
  }
  // SHOW_CURSOR();
  // print_matrix_chars(mat);
}

int main() {
  INT_MATRIX mat = parse_mat_chars();
  INT_MATRIX next = new_int_matrix(height(mat), width(mat));

  run(mat, next);

  printf("%lu\n", count(next));
  clean_int_matrix(next);
  clean_int_matrix(mat);
  return 0;
}
