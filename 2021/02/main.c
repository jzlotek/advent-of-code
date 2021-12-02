#include "aoc.h"

int main() {
  char buf[512];

  int depth = 0, horiz = 0;
  int depth_p2 = 0, horiz_p2 = 0, aim = 0;

  int num;
  while (fgets(buf, 512, stdin)) {
    char *type = strtok(buf, " ");
    num = atoi(strtok(NULL, " "));
    // forward, down, up

    // part1
    horiz += (strcmp(type, "forward") == 0) * num;
    depth -= (strcmp(type, "up") == 0) * num;
    depth += (strcmp(type, "down") == 0) * num;

    // part2
    aim -= (strcmp(type, "up") == 0) * num;
    aim += (strcmp(type, "down") == 0) * num;
    horiz_p2 += (strcmp(type, "forward") == 0) * num;
    depth_p2 += (strcmp(type, "forward") == 0) * num * aim;
  }

  printf("%d\n", horiz * depth);
  printf("%d\n", horiz_p2 * depth_p2);

  return 0;
}
