#include <stdlib.h>
#include <stdio.h>

typedef unsigned long ul;

int has_sum(ul *numbers, ul key, int length) {
  // could reduce this to n lg n if sorting with each iteration
  // but why not just do O(n^2) operations???
  for (unsigned int i = 0; i < length; i++) {
    ul diff = key - numbers[i];
    for (unsigned int j = i + 1; j < length; j++) {
      if (diff == numbers[j])return 1;
    }
  }
  return 0;
}

int __cmpfn(const void *a, const void *b) {
  ul *x = (ul *) a;
  ul *y = (ul *) b;
  if (*x == *y) return 0;
  else if (*x > *y) return 1;
  else return -1;
}

int main() {
  unsigned long values[1000];
  unsigned long a;
  int sum, start, idx, length;
  unsigned long *ptr;

  for (unsigned int i = 0; i < 1000; i++) {
    scanf("%lu\n", &a);
    values[i] = a;
  }

  idx = 25;
  length = 25;
  ptr = &values[0];

  while(idx < 975 && has_sum(ptr, values[idx], length)) {
    idx++;
    ptr++;
  }

  printf("%lu\n", values[idx]);
  ul wrong = values[idx];
  int wrong_idx = idx;

  sum = 0;
  start = 0;
  idx = 0;

  while(start < wrong_idx) {
    if (sum < wrong) {
      sum += values[start + idx];
      idx++;
    } else if (sum > wrong) {
      sum -= values[start];
      start++;
      idx--;
    } else {
      break;
    }
  }

  qsort(&values[start], idx + 1, sizeof(ul), __cmpfn);
  printf("%lu\n", values[start] + values[start + idx]);

  return 0;
}
