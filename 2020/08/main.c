#include <stdlib.h>
#include <stdio.h>
#include <string.h>

enum OPER {
  NOP,
  ACC,
  JMP,
};

typedef struct instruction {
  enum OPER operation;
  int num;
} INS;

struct state {
  int acc;
  int succ;
};

struct state run(INS *instructions, int num_ins) {
  struct state s;
  int times_run[num_ins];
  for (unsigned int i = 0; i < num_ins; i++) {
    times_run[i] = 0;
  }
  int acc = 0;
  int IP = 0;
  int IP_OFFSET = 1;

  while (IP < num_ins && times_run[IP] == 0) {
    IP_OFFSET = 1;
    INS curr_inst = instructions[IP];
    switch(curr_inst.operation) {
      case ACC:
        acc += curr_inst.num;
        break;
      case JMP:
        IP_OFFSET = curr_inst.num;
        break;
      default:
        break;
    }
    times_run[IP] += 1;

    IP+=IP_OFFSET;
  }
  s.acc = acc;
  s.succ = IP == num_ins;
  return s;
}

int main() {
  char op[4];
  int i, n;
  INS instructions[643];

  n = 0;
  INS *inst = (INS*)malloc(sizeof(INS));
  while (scanf("%s %d\n", op, &i) != -1) {
    enum OPER type;
    if (strcmp(op, "nop") == 0) {
      type = NOP;
    } else if (strcmp(op, "acc") == 0) {
      type = ACC;
    } else if (strcmp(op, "jmp") == 0) {
      type = JMP;
    }

    inst->num = i;
    inst->operation = type;
    instructions[n] = *inst;
    n++;
  }
  free(inst);


  struct state s;
  s = run(instructions, 643);
  printf("%d\n", s.acc);

  i = 0;
  enum OPER last;
  for (; !s.succ; i++) {
    last = instructions[i].operation;
    if (last == NOP)
      instructions[i].operation = JMP;
    else if (last == JMP)
      instructions[i].operation = NOP;
    else
      continue;
    s = run(instructions, 643);
    instructions[i].operation = last;
  }
  printf("%d\n", s.acc);
  return 0;
}
