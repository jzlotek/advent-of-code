#include "aoc.h"

int getid(INT_ARRAY line) {
  int id = 0;

  for (unsigned int i = 0; i < line->currsize; i++) {
    id += (arr_get(line, i) == 'B' || arr_get(line, i) == 'R');
    id <<= 1;
  }
  id >>= 1;

  return id;
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
