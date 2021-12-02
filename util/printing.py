import sys

def up():
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()

def print_grid(grid, flush=False):
    xs = [c[0] for c in grid.keys()]
    ys = [c[1] for c in grid.keys()]
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            if (x,y) in grid:
                sys.stdout.write(str(grid[(x,y)]))
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    if flush:
        sys.stdout.flush()
        for y in range(min(ys), max(ys) + 2):
            up()
