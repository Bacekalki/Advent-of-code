from itertools import pairwise, permutations
from functools import cache

@cache
def get_deltas(a, b):
    if a == b:
        return 0, 0
    
    if len(set(a + b).intersection("v><^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"
    
    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3
    bx, by = keypad.index(b) % 3, keypad.index(b) // 3

    return bx-ax, by-ay

@cache
def is_valid_path(a, b, path):
    if len(set(a+b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3

    deltas = {
        "<": (-1, 0),
        ">": (1, 0),
        "v": (0, 1),
        "^": (0, -1)
    }

    for p in path:
        dx, dy = deltas[p]
        ax += dx
        ay += dy

        if ax < 0 or ax >= 3 or ay < 0 or ay >= len(keypad) // 3:
            return False

        if keypad[ay*3+ax] == "X":
            return False
    return True


@cache
def get_all_paths(a, b):
    dx, dy = get_deltas(a, b)
    
    cx = "<" if dx < 0 else ">"
    cy = "^" if dy < 0 else "v"
    
    path = cx * abs(dx) + cy * abs(dy)
    
    return [''.join(my_path) + 'A' for my_path in permutations(path, len(path)) if is_valid_path(a, b, my_path)]


@cache
def get_min_cost(seq, depth):
    seq = "A" + seq
    sum = 0
    
    for a, b in pairwise(seq):
        paths = get_all_paths(a, b)
        
        if depth == 25:
            sum += min(len(p) for p in paths)
        else:
            sum += min(get_min_cost(p, depth + 1) for p in paths)
    
    return sum

def part_2():
    with open('input.txt') as f:
        seqs = f.read().splitlines()

    t = 0
    for seq in seqs:
        t += get_min_cost(seq, 0) * int(seq.replace("A", ""))

    print(t)
    

part_2()