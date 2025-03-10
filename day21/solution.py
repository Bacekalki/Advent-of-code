from queue import Queue
from functools import cache
from itertools import pairwise, permutations

def custom_order(char):
    order = {'^': 1, '>': 1, 'v': 0, '<': 0}
    return order[char]

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

# def custom_order2(char):
#     order = {'^': 0, '>': 0, 'v': 1, '<': 1}
#     return order[char]
@cache
def calculate_price(path):
    second_keypad = [['.', '^', 'A'], ['<', 'v', '>']]
    second_keypad = [['.'] + line + ['.'] for line in second_keypad]
    second_keypad.insert(0, ['.'] * len(second_keypad[0]))
    second_keypad.append(['.'] * len(second_keypad[0]))
    indexes_dict2 = {second_keypad[i][j] : (i, j) for j in range(len(second_keypad[0])) for i in range(len(second_keypad)) if not second_keypad[i][j] == '.'}
    
    return len(translate_code2(path, second_keypad, indexes_dict2))

@cache
def check_order(path, start):
    new_path = sorted(path)
    new_path1 = sorted(path, reverse = True)
    new_path2 = sorted(path, key = custom_order)
    
    
    my_list = []
    
    if validate_paths(''.join(new_path2), start, True):
       my_list.append(''.join(new_path2))
    
    
    if validate_paths(''.join(new_path), start, True):
        my_list.append(''.join(new_path))
    
    if validate_paths(''.join(new_path1), start, True):
        my_list.append(''.join(new_path1))
        
    max = 0
    min_item = new_path
    
    for item in my_list:
        if max < calculate_price(item):
            max = calculate_price(item)
            min_item = item
    
    return min_item
    
def get_neighbours(grid, current):
    directions = [(0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'), (0, -1, '<')]
    x, y = current
    
    return [(x + dx, y + dy, direction) for dx, dy, direction in directions if not grid[x + dx][y + dy] == '.']

@cache
def validate_paths(path: str, start, bool):
    first_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
    second_keypad = [['.', '^', 'A'], ['<', 'v', '>']]
    
    first_keypad = [['.'] + line + ['.'] for line in first_keypad]
    second_keypad = [['.'] + line + ['.'] for line in second_keypad]
    
    first_keypad.insert(0, ['.'] * len(first_keypad[0]))
    first_keypad.append(['.'] * len(first_keypad[0]))
    
    second_keypad.insert(0, ['.'] * len(second_keypad[0]))
    second_keypad.append(['.'] * len(second_keypad[0]))
    
    grid = first_keypad if bool else second_keypad
    
    my_dict = {'v': (1, 0), '>': (0, 1), '<': (0, -1), '^': (-1, 0)}
    x, y = start
    for direction in path:
        if direction == 'A':
            continue
        dx, dy = my_dict[direction]
        if grid[x + dx][y + dy] == '.':
            return False
        x = x + dx
        y = y + dy
    
    return True
        
        

@cache
def shortest_path(start, end, bool):
    first_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
    second_keypad = [['.', '^', 'A'], ['<', 'v', '>']]
    
    first_keypad = [['.'] + line + ['.'] for line in first_keypad]
    second_keypad = [['.'] + line + ['.'] for line in second_keypad]
    
    first_keypad.insert(0, ['.'] * len(first_keypad[0]))
    first_keypad.append(['.'] * len(first_keypad[0]))
    
    second_keypad.insert(0, ['.'] * len(second_keypad[0]))
    second_keypad.append(['.'] * len(second_keypad[0]))
    
    grid = first_keypad if bool else second_keypad
    
    q = Queue()
    visited = set()
    q.put((start, []))
    visited.add(start)
    
    # final_path = []
    
    while not q.empty():
        current, path = q.get()
        
        if current == end:
            if bool:
                path = check_order(''.join(path), start)
            return ''.join(path) + 'A'
        
        neighbours = get_neighbours(grid, current)
        neighbours = sorted(neighbours, key = lambda x : custom_order(x[2]))
        
        for x, y, direction in neighbours:
            if (x, y) not in visited:
                q.put(((x, y), path + [direction]))
                visited.add((x, y))
        
        #return list(filter(lambda path: validate_paths(grid, path, start), [perm + ['A'] for perm in permutations(final_path, len(final_path))]))
        

# @cache
# def solve(char1, char2, depth):


def translate_code2(path, keypad, indexes_dict2):
    my_path = 'A' + ''.join(path)
    whole_path = ''
    for i in range(len(my_path) - 1):
        char1 = my_path[i]
        char2 = my_path[i + 1]
        whole_path += ''.join(shortest_path(indexes_dict2[char1], indexes_dict2[char2], False))
    
    return whole_path


@cache
def get_deltas(a, b):
    if a == b:
        return 0, 0

    if len(set(a+b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3
    bx, by = keypad.index(b) % 3, keypad.index(b) // 3

    return bx-ax, by-ay


def get_all_paths(a, b):
    dx, dy = get_deltas(a, b)

    cx = "<" if dx < 0 else ">"
    cy = "^" if dy < 0 else "v"

    nx = cx * abs(dx) + cy * abs(dy)
    possible = []
    for p in permutations(nx):
        if is_valid_path(a, b, p):
            possible.append("".join(p) + "A")

    return possible
    

@cache
def translate_code(path, depth):
    
    my_path = path + "A"
    first_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
    second_keypad = [['.', '^', 'A'], ['<', 'v', '>']]
    
    first_keypad = [['.'] + line + ['.'] for line in first_keypad]
    second_keypad = [['.'] + line + ['.'] for line in second_keypad]
    
    first_keypad.insert(0, ['.'] * len(first_keypad[0]))
    first_keypad.append(['.'] * len(first_keypad[0]))
    
    indexes_dict1 = {first_keypad[i][j] : (i, j) for j in range(len(first_keypad[0])) for i in range(len(first_keypad)) if not first_keypad[i][j] == '.'}
    
    second_keypad.insert(0, ['.'] * len(second_keypad[0]))
    second_keypad.append(['.'] * len(second_keypad[0]))
    
    indexes_dict2 = {second_keypad[i][j] : (i, j) for j in range(len(second_keypad[0])) for i in range(len(second_keypad)) if not second_keypad[i][j] == '.'}
    
    correct_keypad = first_keypad if depth == 0 else second_keypad
    correct_dict = indexes_dict1 if depth == 0 else indexes_dict2
   
    
    sum = 0
    for a,b in pairwise(my_path):
        best = shortest_path(correct_dict[a], correct_dict[b], depth == 0)
        print(best)
        if depth == 3:
            sum += len(best)
        else:
            sum += translate_code(best, depth + 1)
        
    return sum


@cache
def get_min_cost(seq, depth):
    ret = 0
    seq = "A" + seq
    for a, b in pairwise(seq):
        ps = get_all_paths(a, b)
        if depth == 0:
            ret += min(len(p) for p in ps)
        else:
            ret += min(get_min_cost(p, depth-1) for p in ps)
    return ret

with open('input.txt', 'r') as file:
    codes = [line.strip('\n') for line in file.readlines()]
    
    first_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
    second_keypad = [['.', '^', 'A'], ['<', 'v', '>']]
    
    
    first_keypad = [['.'] + line + ['.'] for line in first_keypad]
    second_keypad = [['.'] + line + ['.'] for line in second_keypad]
    
    first_keypad.insert(0, ['.'] * len(first_keypad[0]))
    first_keypad.append(['.'] * len(first_keypad[0]))
    
    indexes_dict1 = {first_keypad[i][j] : (i, j) for j in range(len(first_keypad[0])) for i in range(len(first_keypad)) if not first_keypad[i][j] == '.'}
    
    second_keypad.insert(0, ['.'] * len(second_keypad[0]))
    second_keypad.append(['.'] * len(second_keypad[0]))
    
    indexes_dict2 = {second_keypad[i][j] : (i, j) for j in range(len(second_keypad[0])) for i in range(len(second_keypad)) if not second_keypad[i][j] == '.'}
    
    value = 0
    new_path = ''
    for code in codes:
        sum = get_min_cost(code, 25)
        
        # print(first_transl)
        # print(len(third_transl))
        
        value += sum * int(code[:-1])
    
    
    print(value)
    
    # print(calculate_price('^^<<', second_keypad, indexes_dict2))
        
        
        
    
    
        
        
        
        
        
    

    
    
    