#include "aoc.h"

int main() {
  INT_MATRIX mat = parse_mat_chars();
  HIDE_CURSOR();
  int i = 0;
  while (i<100) {
    print_matrix_chars_loop(mat);
    ++i;
  }
  print_matrix_chars(mat);
  SHOW_CURSOR();

  printf("%c\n", mat_get(mat, -1, -1));

  arrsort(mat->data[0]);
  print_arr_chars(mat->data[0]);



  clean_int_matrix(mat);
  return 0;
}
