#include "aoc.h"

int main() {
  INT_MATRIX arr = parse_mat_chars();
  print_matrix_chars(arr);
  clean_int_matrix(arr);

  return 0;
}
