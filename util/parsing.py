def parse_list(data_type=int, delim=','):
    arr = []
    with open('input', 'r') as f:
        for l in f:
            arr.extend([data_type(x) for x in l.strip().split(delim)])
    return arr

def parse_as_str_list():
    with open('input', 'r') as f:
        arr = f.readlines()
    return [s.strip() for s in arr]

def parse_as_str():
    s = ""
    with open('input', 'r') as f:
        for l in f:
            s += l
    return s

def parse_list2d(data_type=int, delim=','):
    arr = []
    with open('input', 'r') as f:
        for l in f:
            arr.append([data_type(x) for x in l.strip().split(delim)])
    return arr

