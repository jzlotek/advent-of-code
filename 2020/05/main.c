#include "aoc.h"

int getid(INT_ARRAY line) {
  int row, col;
  int start, end;
  int div;

  div = 64;
  start = 0;
  end = 127;
  for (unsigned int i = 0; i < 7; i++) {
    if (arr_get(line, i) == 'F') {
      end -= div;
    } else {
      start += div;
    }
    div /= 2;
  }
  row = start;

  div = 4;
  start = 0;
  end = 7;
  for (unsigned int i = 7; i < line->currsize; i++) {
    if (arr_get(line, i) == 'L') {
      end -= div;
    } else {
      start += div;
    }
    div /= 2;
  }
  col = start;

  return row * 8 + col;
}
int main() {
  INT_MATRIX mat = parse_mat_chars();
  INT_ARRAY nums = new_int_array(0);
  for (unsigned int i = 0; i < mat->currheight; i++) {
    append(nums, getid(mat->data[i]));
  }
  arrsort(nums);
  printf("%d\n", arr_get(nums, -1));
  for (unsigned int i = 1; i < nums->currsize - 1; i++) {
    if (arr_get(nums, i) - arr_get(nums, i - 1) == 2) {
      printf("%d\n", arr_get(nums, i) - 1);
      break;
    }
  }

  clean_int_matrix(mat);
  clean_int_array(nums);
  return 0;
}
