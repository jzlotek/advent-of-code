#include "aoc.h"

#define ul long long

ul count(INT_ARRAY jolts, ul *cache) {
  ul sum = 1;
  int j = 0;
  cache[0] = 1;
  for (unsigned int i = 1; i < len(jolts); i++) {
    while (arr_get(jolts, i) - arr_get(jolts, j) > 3) {
      sum -= cache[j];
      j++;
    }
    cache[i] = sum;
    sum += cache[i];
  }
  return cache[jolts->currsize - 1];
}

int main() {
  INT_ARRAY jolts = parse_arr("\n");

  append(jolts, 0);
  arrsort(jolts);
  append(jolts, arr_get(jolts, -1) + 3);
  int one, three;

  one = 0;
  three = 0;

  for (unsigned int i = 1; i < len(jolts); i++){
    int diff = arr_get(jolts, i) - arr_get(jolts, i - 1);
    one += diff == 1;
    three += diff == 3;
  }
  printf("%d\n", one * three);


  ul cache[jolts->currsize];
  for (unsigned int i = 0; i < jolts->currsize; i++) {
    cache[i] = 0;
  }

  printf("%lld\n", count(jolts, cache));
  clean_int_array(jolts);
  return 0;
}
