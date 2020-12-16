#include "aoc.h"

long long getnth(INT_ARRAY nums, long n) {
  long last;

  long long *current = (long long*)malloc(sizeof(long long) * n);
  long long *previous = (long long*)malloc(sizeof(long long) * n);

  unsigned long i;
  for (i = 0; i < n; i++) {
    previous[i] = -1;
    current[i] = 0;
  }

  for (i = 0; i < len(nums); i++) {
    int num = arr_get(nums, i);
    current[num] =  i + 1;
    previous[num] = -1;
  }
  last = arr_get(nums, -1);

  for (i = len(nums); i < n; i++) {
    if (current[last] == 0 || previous[last] == -1) {
      last = 0;
    } else {
      last = current[last] - previous[last];
    }

    previous[last] = ((current[last] == 0) * -1) + ((current[last] != 0) * current[last]);
    current[last] = i + 1;
  }

  free(current);
  free(previous);
  return last;
}

int main() {
  INT_ARRAY nums = parse_arr(",");

  printf("%lld\n", getnth(nums, 2020));
  printf("%lld\n", getnth(nums, 30000000));

  clean_int_array(nums);
  return 0;
}
