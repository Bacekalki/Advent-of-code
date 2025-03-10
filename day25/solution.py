from copy import deepcopy

def is_key(grid):
    return all(point == '.' for point in grid[0])

def get_column(grid, index):
    return [grid[i][index] for i in range(len(grid))]

def get_heights(grid):
    return [sum(1 for point in get_column(grid, index) if point == '#') - 1  for index in range(len(grid[0]))]

def fit(key, lock):
    return all(key[i] + lock[i] < 6 for i in range(len(key)))

with open("input.txt", 'r') as file:
    lines = file.readlines()
    current = []
    keys = []
    locks = []
    for line in lines:
        if line == '\n':
            if is_key(current):
                keys.append(deepcopy(current))
            else:
                locks.append(deepcopy(current))
                
            current.clear()
        else:
            current.append(list(line.strip('\n')))
    
    if len(current) > 0:
        if is_key(current):
            keys.append(current)
        else:
            locks.append(current)
    
    keys_map = list(map(get_heights, keys))
    locks_map = list(map(get_heights, locks))
    
    counter = 0
    for key in keys_map:
        for lock in locks_map:
            if fit(key, lock):
                counter += 1
    
    print(counter)
        
            
            
        

            