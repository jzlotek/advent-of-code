#include <stdio.h>
// AOC Day 2
// jzlotek

int main() {
  int count_a, count_b;
  int a, b;
  char c;

  count_a = 0;
  count_b = 0;

  char buf[32];
  while (scanf("%d-%d %c: %s\n", &a, &b, &c, buf) != -1) {
    int lcount, i;

    lcount = 0;
    i = 0;
    while(buf[i] != '\0' && buf[i] != '\n') {
      if (buf[i] == c) lcount++;
      i++;
    }
    count_a += lcount >= a && lcount <= b; // part1
    count_b += buf[a - 1] == c ^ buf[b - 1] == c; // part2
  }

  printf("%d %d\n", count_a, count_b);

  return 0;
}
