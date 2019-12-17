import itertools
import copy
import sys
sys.path.append('../..')
from util.parsing import parse_list


def parse_ins(ins):
    i = '%05d' % ins
    return int(i[0]), int(i[1]), int(i[2]), int(i[3:])


class IntCode:

    def __init__(self, ops):
        self.ops = copy.deepcopy(ops)
        self.ip = 0
        self.buffer = []
        self.rel_base = 0
    
    def get(self, idx):
        if len(self.ops) <= idx:
            return 0
        return self.ops[idx]


    def get_val(self, ip, mode, op, pos):
        if (op in [1,2,7,8] and pos == 3) or (op == 3 and pos == 1):
            if mode == 2:
                return ip + self.rel_base
            else:
                return ip
        if mode == 1:
            return ip
        elif mode == 2:
            return self.get(ip + self.rel_base)
        else:
            return self.get(ip)

    def write(self, index, value):
        idx = index
        if len(self.ops) <= idx:
            self.ops = [*self.ops, *[0 for _ in range(idx - len(self.ops) + 1)]]
        self.ops[idx] = value

    def safe_get(self, s, e):
        if e < len(self.ops):
            return self.ops[s:e]
        offset = 0
        while e - offset >= len(self.ops):
            offset += 1
        return self.ops[s:e] + [0 for _ in range(offset - 1)]
    
    def is_done(self):
        A, B, C, op = parse_ins(self.ops[self.ip])
        return op == 99

    def run(self, input_instruction):
        while True:
            A, B, C, op = parse_ins(self.ops[self.ip])
            if op == 99:
                break
            i1, i2, output = self.safe_get(self.ip + 1, self.ip + 4)
            a = self.get_val(i1, C, op, 1)
            b = self.get_val(i2, B, op, 2)
            output = self.get_val(output, A, op, 3)

            count = 4

            if op == 1:  # add
                self.write(output, a + b)
            elif op == 2:  # mult
                self.write(output, a * b)
            elif op == 3:  # read from input into address
                self.write(a, input_instruction)
                count = 2
            elif op == 4:  # write to stdout the address
                self.ip += 2
                return a
            elif op in [5, 6]:  # jmp if true/false
                count = 3
                if (a != 0 and op == 5) or (a == 0 and op == 6):
                    self.ip = b
                    continue
            elif op == 7:  # set 1 if a < b
                self.write(output, 1 if a < b else 0)
            elif op == 8:  # set 1 if a == b
                self.write(output, 1 if a == b else 0)
            elif op == 9:
                self.rel_base += a
                count = 2
            else:
                print(f'error parsing op: {op}')
            self.ip += count
