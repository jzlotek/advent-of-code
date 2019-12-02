import itertools
import copy

with open("input", 'r') as f:
    orig = [int(c) for c in f.readline().split(',')]

ops = copy.deepcopy(orig)

print(','.join([str(op) for op in ops]))


def f(aa, bb):
    ops[1] = aa
    ops[2] = bb
    i = 0
    while i < len(ops):
        if ops[i] == 99:
            break
        a = ops[i+1]
        b = ops[i+2]
        c = ops[i+3]
        if ops[i] == 1:
            ops[c] = ops[a]+ops[b]
            i += 4
            continue
        if ops[i] == 2:
            ops[c] = ops[a]*ops[b]
            i += 4
            continue

        i += 1

    if ops[0] == 19690720:
        print(aa, bb)


for (a, b) in itertools.product(range(100), range(99)):
    ops = copy.deepcopy(orig)
    f(a, b)
