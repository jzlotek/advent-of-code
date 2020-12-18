#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "aoc.h"

typedef struct __range {
  int low;
  int high;
} range;

long compare(int value, range *ranges, int n) {
  for (unsigned int i = 0; i < n; i++) {
    if (value >= ranges[i].low && ranges[i].high >= value) {
      return 0;
    }
  }
  return value;
}

int get_idx(INT_ARRAY row) {
  for (unsigned int i = 0; i < len(row); i++) {
    if (arr_get(row, i))
      return i;
  }
  perror("get_idx not found");
}

void process_sol(INT_MATRIX tickets, INT_MATRIX sieve, range *ranges, int num) {
  int num_work;
  for (unsigned int r = 0; r < num; r += 2) {
    num_work = 0;
    range a = ranges[r];
    range b = ranges[r + 1];

    for (unsigned int j = 0; j < width(tickets); j++) {
      for (unsigned int i = 0; i < height(tickets); i++) {
        int currval = mat_get(tickets, i, j);
        if ((currval < a.low || currval > a.high) && (currval < b.low || currval > b.high)) {
          sieve->data[r / 2]->data[j] = 0;
          break;
        } 
      }
    }
  }

  int j;
  while(sum_mat(sieve) > 20) {
    for (unsigned int i = 0; i < height(sieve); i++) {
      if (sum(sieve->data[i]) == 1) {
        j = 0;
        while (j < width(sieve) && sieve->data[i]->data[j] == 0) {
          j++;
        }
        for (unsigned int row = 0; row < height(sieve); row++) {
          if (row == i) continue;
          sieve->data[row]->data[j] = 0;
        }
      }
    }
  }
}

int main() {
  int low1, high1, low2, high2, val;
  int i;
  char buf[512];

  range *ranges = (range*)malloc(sizeof(range) * 40);

  i = 0;
  while (i < 40 && scanf("%*[a-z ]: %d-%d or %d-%d\n", &low1, &high1, &low2, &high2) != -1) {
    ranges[i].low = low1;
    ranges[i].high = high1;
    ranges[i+1].low = low2;
    ranges[i+1].high = high2;
    i += 2;
  }

  while(1) {
    fgets(buf, 512, stdin);
    if (strcmp(buf, "nearby tickets:\n") == 0)
      break;
  }

  char *tok;
  long long error = 0;
  int isvalid;
  int myticket[20] = {61,151,137,191,59,163,89,83,71,179,67,149,197,167,181,173,53,139,193,157};

  INT_ARRAY currtick;
  INT_MATRIX alltickets = new_int_matrix(0, 20);

  int field, trash, numtickets;
  numtickets = 0; trash = 0;
  while (fgets(buf, 512, stdin) != NULL) {
    if (trash == 0) {
      currtick = new_int_array(20);
    }
    tok = strtok(buf, ",");
    trash = 0;
    i = 0;
    while (tok != NULL) {
      val = atoi(tok);
      currtick->data[i] = val;
      isvalid = compare(val, ranges, 40);
      if (isvalid != 0) trash = 1;
      error += isvalid;
      tok = strtok(NULL, ",");
      i++;
    }
    if (!trash) {
      append_row(alltickets, currtick);
    }
  }

  printf("%lld\n", error);

  INT_MATRIX sieve = new_int_matrix(20, 20);
  for (unsigned int r = 0; r < 20; r++) {
    for (unsigned int c = 0; c < 20; c++) {
      sieve->data[r]->data[c] = 1;
    }
  }

  process_sol(alltickets, sieve, ranges, 40);

  long prod = 1;
  for (i = 0; i < 6; i++) {
    prod *= myticket[get_idx(sieve->data[i])];
  }

  printf("%lld\n", prod);

  clean_int_matrix(alltickets);
  free(ranges);

  return 0;
}