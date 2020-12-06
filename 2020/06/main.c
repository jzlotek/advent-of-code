#include "aoc.h"

int count(INT_MATRIX mat) {
  int count = 0;
  for (unsigned int i = 0; i < mat->currheight; i++) {
    INT_ARRAY groupcnts = new_int_array(26);
    while (i < mat->currheight && mat->data[i]->currsize != 0) {
      INT_ARRAY line = mat->data[i];
      for (unsigned int c = 0; c < line->currsize; c++)
        groupcnts->data[arr_get(line, c) - 97] = 1;
      i++;
    }
    count += sum(groupcnts);
    clean_int_array(groupcnts);
  }

  return count;
}

int count_b(INT_MATRIX mat) {
  int count = 0;
  int numInGroup;
  for (unsigned int i = 0; i < mat->currheight; i++) {
    INT_ARRAY groupcnts = new_int_array(26);
    numInGroup = 0;
    while (i < mat->currheight && mat->data[i]->currsize != 0) {
      INT_ARRAY line = mat->data[i];
      for (unsigned int c = 0; c < line->currsize; c++)
        groupcnts->data[arr_get(line, c) - 97] += 1;
      numInGroup++;
      i++;
    }
    divarr(groupcnts, numInGroup);
    count += sum(groupcnts);
    clean_int_array(groupcnts);
  }

  return count;
}

int main() {
  INT_MATRIX mat = parse_mat_chars();

  printf("%d\n", count(mat));
  printf("%d\n", count_b(mat));


  clean_int_matrix(mat);
  return 0;
}
