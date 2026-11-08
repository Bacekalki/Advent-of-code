from collections import defaultdict
from itertools import combinations

def calcManhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    
    return abs(x1 - x2) + abs(y1 - y2)

def are_on_the_same_line(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area == 0

def eval_point(a, my_dict):
    for value in my_dict.values():
        for b, c in combinations(value, 2):
            if are_on_the_same_line(a, b, c):
                    return True
            
        
        
        
        
    
with open("input.txt", 'r') as file:
    grid = [line.strip('\n') for line in file.readlines()]
    my_dict = defaultdict(lambda: [])
    antinodes = set()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j] == '.':
                my_dict[grid[i][j]].append((i, j))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                if eval_point((i, j), my_dict):
                    antinodes.add((i, j))

    
    print(len(antinodes))
                    
    
    
    

