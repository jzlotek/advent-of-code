#include <stdio.h>
#include <stdlib.h>

#define HEADINGS 771

typedef struct __heading {
  char c;
  int num;
} Heading;

long navigate(Heading *headings, int len) {
  long x, y, dx, dy, tmp;
  x = 0, y = 0, dx = 1, dy = 0;

  for (unsigned int i = 0; i < len; i++) {
    Heading curr = headings[i];

    x += curr.num * ((curr.c == 'E') + ((curr.c == 'W') * -1) + ((curr.c == 'F') * dx));
    y += curr.num * ((curr.c == 'S') + ((curr.c == 'N') * -1) + ((curr.c == 'F') * dy));
    switch(curr.c) {
      case 'L':
        for (int r = 0; r < curr.num / 90; r++) {
          tmp = dy;
          dy = -dx;
          dx = tmp;
        }
        break;
      case 'R':
        for (int r = 0; r < curr.num / 90; r++) {
          tmp = dx;
          dx = -dy;
          dy = tmp;
        }
        break;
      default:
        break;
    }
  }

  return abs(x) + abs(y);
}

long navigate2(Heading *headings, int len) {
  long x, y, dx, dy, tmp;
  x = 0, y = 0, dx = 10, dy = -1;

  for (unsigned int i = 0; i < len; i++) {
    Heading curr = headings[i];

    x += curr.num * ((curr.c == 'F') * dx);
    y += curr.num * ((curr.c == 'F') * dy);
    dx += curr.num * ((curr.c == 'E') + ((curr.c == 'W') * -1));
    dy += curr.num * ((curr.c == 'S') + ((curr.c == 'N') * -1));
    switch(curr.c) {
      case 'L':
        for (int r = 0; r < curr.num / 90; r++) {
          tmp = dy;
          dy = -dx;
          dx = tmp;
        }
        break;
      case 'R':
        for (int r = 0; r < curr.num / 90; r++) {
          tmp = dx;
          dx = -dy;
          dy = tmp;
        }
        break;
      default:
        break;
    }
  }

  return abs(x) + abs(y);
}

int main() {
  Heading headings[771];
  char c;
  int num;

  for (unsigned int i = 0; i < HEADINGS; ++i) {
    scanf("%c%d\n", &c, &num);
    headings[i].c = c;
    headings[i].num = num;
  }

  printf("%ld\n", navigate(headings, HEADINGS));
  printf("%ld\n", navigate2(headings, HEADINGS));

  return 0;
}
