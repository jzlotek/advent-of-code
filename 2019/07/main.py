import itertools
import copy
import sys
sys.path.append('../..')
from util.parsing import parse_list

orig = parse_list()

ops = copy.deepcopy(orig)

def parse_ins(ins):
    i = '%05d' % ins
    return int(i[0]), int(i[1]), int(i[2]), int(i[3:])

def f(input_instruction):
    i = 0
    while i < len(ops):
        A, B, C, op = parse_ins(ops[i])
        if op == 99:
            break
        i1, i2, output = ops[i + 1: i + 4]
        #print('i1', i1, 'i2', i2)
        a = ops[i1] if C == 0 else i1

        #print('a', a, 'out', output)
        if op not in [3,4]:
            b = ops[i2] if B == 0 else i2

        count = 4

        if op == 1: # add
            ops[output] = a + b
        elif op == 2: # mult
            ops[output] = a * b
        elif op == 3: # read from input into address
            ops[i1] = input_instruction
            count = 2
        elif op == 4: # write to stdout the address
            print(a)
            count = 2
        elif op == 5 or op == 6: # jmp if true/false
            count = 3
            if (a != 0 and op == 5) or (a == 0 and op == 6):
                i = b
                #print(i)
                #print(op, a, b, ops[i], i1, i2)
                continue
        elif op == 7: # set 1 if a < b
            ops[output] = (1 if a < b else 0)
        elif op == 8: # set 1 if a == b
            ops[output] = (1 if a == b else 0)
        else:
            pass
            #print(f'error parsing op: {op}')
        i += count

f(1)
ops = copy.deepcopy(orig)
f(5)
