import itertools
import copy
import sys
sys.path.append('../..')
from util.parsing import parse_list

orig = parse_list()

ops = copy.deepcopy(orig)
#ops = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

def parse_ins(ins):
    i = '%05d' % ins
    return int(i[0]), int(i[1]), int(i[2]), int(i[3:])

class IntCode:

    def __init__(self, ops):
        self.ops = copy.deepcopy(ops)
        self.ip = 0
        self.rel_base = 0

    def get_val(self, ip, mode):
        if mode == 1:
            return ip
        elif mode == 2:
            if ip + self.rel_base >= len(self.ops):
                return 0
            return self.ops[ip + self.rel_base]
        else:
            if ip >= len(self.ops):
                return 0
            return self.ops[ip]

    def write(self, index, mode, value):
        if len(self.ops) <= index:
            self.ops = [*ops, *[0 for _ in range(index - len(self.ops) + 1)]]
        if mode == 0:
            self.ops[index] = value
        elif mode == 2:
            self.ops[index + self.rel_base] = value

    def get(self, index):
        if len(self.ops) <= index:
            self.ops = [*ops, *[0 for _ in range(index - len(self.ops) + 1)]]

    def safe_get(self, s, e):
        if e < len(self.ops):
            return self.ops[s:e]
        offset = 0
        while e - offset >= len(self.ops):
            offset += 1
        return self.ops[s:e] + [0 for _ in range(offset - 1)]

    def run(self, input_instruction):
        while self.ip < len(self.ops):
            print('OP', self.ops[self.ip])
            A, B, C, op = parse_ins(self.ops[self.ip])
            if op == 99:
                break

            i1, i2, output = self.safe_get(self.ip + 1, self.ip + 4)
            #print(op, i1, i2, output, rel_base)

            if op in [1,2,7,8,9]:
                A = 1 if A != 2 else 2
            if op == 3:
                C = 1 if C != 2 else 2
            a = self.get_val(i1, C)
            b = self.get_val(i2, B)

            output = self.get_val(output, A)
            #print(a,b,output)


            count = 4

            if op == 1: # add
                print('ADD', a, b, output)
                self.write(output, A, a + b)
            elif op == 2: # mult
                print('MULT', a, b, output)
                self.write(output, A, a * b)
            elif op == 3: # read from input into address
                print('READ', input_instruction, i1)
                self.write(a, C, input_instruction)
                count = 2
            elif op == 4: # write to stdout the address
                print('OUTPUT', a)
                count = 2
            elif op == 5 or op == 6: # jmp if true/false
                count = 3
                if (a != 0 and op == 5) or (a == 0 and op == 6):
                    print('JMP', a, b)
                    i = b
                    continue
            elif op == 7: # set 1 if a < b
                print('SLT', a, b, output)
                self.write(output, A, 1 if a < b else 0)
            elif op == 8: # set 1 if a == b
                print('SEQ', a, b, output)
                self.write(output, A, 1 if a == b else 0)
            elif op == 9:
                print('REL', a, self.rel_base)
                self.rel_base += a
                count = 2
            else:
                print(f'error parsing op: {op}')
            self.ip += count

computer = IntCode(ops)
computer.run(1)
#f(5)
