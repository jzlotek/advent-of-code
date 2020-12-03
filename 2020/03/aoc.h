#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HIDE_CURSOR() fputs("\e[?25l", stdout);
#define SHOW_CURSOR() fputs("\e[?25h", stdout);

struct int_arr {
  int *data;
  unsigned int maxsize;
  unsigned int currsize;
};

typedef struct int_arr *INT_ARRAY;

struct int_matrix {
  INT_ARRAY *data;
  unsigned int maxheight;
  unsigned int currheight;
  unsigned int currwidth;
};

typedef struct int_matrix *INT_MATRIX;


int len(INT_ARRAY int_arr) {
  return int_arr->currsize;
}

int height(INT_MATRIX matrix) {
  return matrix->currheight;
}

int width(INT_MATRIX matrix) {
  return matrix->currwidth;
}

INT_ARRAY new_int_array(unsigned int length) {
  INT_ARRAY arr = (INT_ARRAY)malloc(sizeof(struct int_arr));
  int start = 2;
  // always make multiple of 2
  while (start < length) {
    start *= 2;
  }
  arr->data = (int*)malloc(sizeof(int) * start);
  if (arr->data == NULL) {
    perror("Failed to allocate array");
    exit(1);
  }
  for (unsigned int i = 0; i < length; ++i)
    arr->data[i] = 0;
  arr->currsize = length;
  arr->maxsize = start;
  return arr;
}

INT_MATRIX new_int_matrix(unsigned int height, unsigned int width) {
  INT_MATRIX arr = (INT_MATRIX)malloc(sizeof(struct int_matrix));
  int start = 2;
  while (start < height) {
    start *= 2;
  }
  arr->data = (INT_ARRAY*)malloc(sizeof(INT_ARRAY) * start);
  if (arr->data == NULL) {
    perror("Failed to allocate matrix");
    exit(1);
  }
  for (unsigned int i = 0; i < height; ++i)
    arr->data[i] = new_int_array(width);

  arr->currwidth = width;
  arr->currheight = height;
  arr->maxheight = start;
  return arr;
}

void append(INT_ARRAY arr, int val) {
  if (len(arr) == arr->maxsize) {
    arr->data = (int*)realloc(arr->data, arr->maxsize * 2 * sizeof(int));
    if (arr->data == NULL) {
      perror("Failed to reallocate array");
      exit(1);
    }
    arr->maxsize *= 2;
  }
  arr->data[arr->currsize] = val;
  arr->currsize++;
}

int arr_get(INT_ARRAY arr, int idx) {
  if (idx >= 0 && idx < arr->currsize)
    return arr->data[idx];

  if (idx < 0) {
    int tidx = arr->currsize + idx;
    if (tidx >= 0 && tidx < arr->currsize) {
      return arr->data[tidx];
    } else {
      perror("idx out of range");
      exit(1);
    }
  }
  perror("idx out of range");
  exit(1);
}

int mat_get(INT_MATRIX mat, int r, int c) {
  if (r >= 0 && r < mat->currheight)
    return arr_get(mat->data[r], c);

  if (r < 0) {
    int tr = mat->currheight + r;
    if (tr >= 0 && tr < mat->currheight) {
      return arr_get(mat->data[tr], c);
    } else {
      perror("idx out of range");
      exit(1);
    }
  }
  perror("idx out of range");
  exit(1);
}

void apppend_col(INT_MATRIX arr, INT_ARRAY col) {
  if (len(col) != arr->currheight) {
      perror("Length of row does not match matrix height");
      exit(1);
  }
  for (unsigned int i = 0; i < height(arr); i++) {
    append(arr->data[i], col->data[i]);
  }
  arr->currwidth++;
}

void append_row(INT_MATRIX arr, INT_ARRAY row) {
  if (len(row) != arr->currwidth) {
      perror("Length of row does not match matrix width");
      exit(1);
  }
  if (height(arr) == arr->maxheight) {
    arr->data = (INT_ARRAY*)realloc(arr->data, arr->maxheight * 2 * sizeof(INT_MATRIX));
    if (arr->data == NULL) {
      perror("Failed to reallocate array");
      exit(1);
    }
    arr->maxheight *= 2;
  }
  arr->data[arr->currheight] = row;
  arr->currheight++;
}

void print_arr(INT_ARRAY arr) {
  printf("[");
  for (unsigned int i = 0; i < arr->currsize; ++i) {
    printf("%d", arr->data[i]);
    if (i < arr->currsize - 1)
      printf(", ");
  }
  printf("]\n");
}

int __cmpfn(const void *a, const void *b) {
  int *x = (int *) a;
  int *y = (int *) b;
  return *x - *y;
}

void arrsort(INT_ARRAY arr) {
  qsort(arr->data, arr->currsize, sizeof(int), __cmpfn);
}

void print_arr_chars(INT_ARRAY arr) {
  for (unsigned int i = 0; i < arr->currsize; ++i) {
    printf("%c", arr->data[i]);
  }
  printf("\n");
}

void print_matrix(INT_MATRIX arr) {
  for (unsigned int i = 0; i < arr->currheight; ++i) {
    print_arr(arr->data[i]);
  }
}

void print_matrix_chars(INT_MATRIX arr) {
  for (unsigned int i = 0; i < arr->currheight; ++i) {
    print_arr_chars(arr->data[i]);
  }
}

void print_matrix_chars_loop(INT_MATRIX mat) {
  // Prints the matrix but with flushing so it can be updated on the
  // screen. use HIDE_CURSOR() before and  SHOW_CURSOR() after
  print_matrix_chars(mat);
  printf("\033[%dA", mat->currheight);
  fflush(stdout);
}

void clean_int_array(INT_ARRAY arr) {
  free(arr->data);
  free(arr);
}

void clean_int_matrix(INT_MATRIX mat) {
  for (unsigned int i = 0; i < mat->currheight; i++) {
    clean_int_array(mat->data[i]);
  }
  free(mat->data);
  free(mat);
}


INT_ARRAY parse_arr(char *delim) {
  INT_ARRAY arr = new_int_array(0);
  int x;
  while(scanf("%d\n", &x) == 1) {
    append(arr, x);
  }
  return arr;
}

INT_MATRIX parse_mat(char *delim) {
  INT_MATRIX arr = new_int_matrix(0, 0);
  int x;
  char *tok;
  int MAX_LENGTH = 512;

  // hopefully lines arent longer than this....
  char buf[MAX_LENGTH];
  while(fgets(buf, MAX_LENGTH, stdin) != NULL) {
    tok = strtok(buf, delim);
    INT_ARRAY row = new_int_array(0);
    while (tok != NULL) {
      x = atoi(tok);
      append(row, x);
      tok = strtok(NULL, delim);
    }
    arr->currwidth = len(row);
    append_row(arr, row);
  }
  return arr;
}

INT_MATRIX parse_mat_chars() {
  INT_MATRIX arr = new_int_matrix(0, 0);
  int MAX_LENGTH = 512;

  // hopefully lines arent longer than this....
  char buf[MAX_LENGTH];
  while(fgets(buf, MAX_LENGTH, stdin) != NULL) {
    INT_ARRAY row = new_int_array(0);

    int i = 0;
    while (buf[i] != '\n' && buf[i] != EOF && buf[i] != '\0') {
      append(row, (int)buf[i]);
      ++i;
    }

    arr->currwidth = len(row);
    append_row(arr, row);
  }
  return arr;
}

