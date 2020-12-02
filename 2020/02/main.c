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
    if (lcount >= a && lcount <= b) count_a++; // part1
    if (buf[a - 1] != buf[b - 1] && (buf[a - 1] == c || buf[b - 1] == c)) count_b++; // part2
  }

  printf("%d %d\n", count_a, count_b);

  return 0;
}
