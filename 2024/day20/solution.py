from queue import Queue as StandardQueue
from collections import Counter

 
def find_start_and_end(grid):
    start = (0, 0)
    end = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = i, j
            
            if grid[i][j] == 'E':
                end = i, j
    
    return start, end

def get_neighbours(grid, current):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = current 
    
    return [(x + dx, y + dy) for dx, dy in directions if not grid[x + dx][y + dy] == '#']

def get_count_of_walls(grid, current):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = current
    
    return sum(1 for dx, dy in directions if grid[x + dx][y + dy] == '#')

def get_all_neighbours(grid, current):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = current
    
    return [(x + dx, y + dy) for dx, dy in directions if 1 <= x + dx < len(grid) - 1 and 1 <= y + dy < len(grid[0]) - 1 and grid[x + dx][y + dy] == '#' and get_count_of_walls(grid, (x + dx, y + dy)) < 3]


def find_path(grid, start, end):
    q = StandardQueue()
    visited = set()
    q.put((start, [start]))
    visited.add(start)
    
    while not q.empty():
        current, path = q.get()
        
        if current == end:
            return path
        
        neighbours = get_neighbours(grid, current)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                q.put((neighbour, path + [neighbour]))

# def get_possible_cheats(grid, path):
#     possible_cheats = set()
#     for point in path:
#         neighbours = get_all_neighbours(grid, point)
#         for neighbour in neighbours:
#             possible_cheats.add(neighbour)
    
    
#     return possible_cheats

def manhattan_distance(point1, point2):
    x, y = point1
    x1, y1 = point2
    
    return abs(x - x1) + abs(y - y1)
    
    


        
        
        
    

if __name__ == '__main__':
    with open("input.txt", 'r') as file:
        grid = [list(line.strip('\n')) for line in file.readlines()]
        start, end = find_start_and_end(grid)
        path = find_path(grid, start, end)
        # possible_cheats = get_possible_cheats(grid, path)
        cheapest = 9469
        saved = []
        
        for i in range(len(path)):
            for j in range(i + 1, len(path)):
                if manhattan_distance(path[i], path[j]) <= 20:
                    saved.append(j - i - manhattan_distance(path[i], path[j]))
        
        c = list(filter(lambda x: x >= 100, saved))
        print(len(c))
        