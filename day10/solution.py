from queue import Queue

def find_zeros(grid):
    zeros = [(i, j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == '0']
    return zeros

def get_neighbours(grid, point):
    x, y = point
    return [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if not grid[x + dx][y + dy] == '.']

def calculate_score(grid, starting_point):
    q = Queue()
    q.put(starting_point)
    visited = set()
    count = 0
    
    while not q.empty():
        current = q.get()
        x, y = current
        visited.add(current)
        if grid[x][y] == '9':
            count += 1
        
        neighbours = get_neighbours(grid, current)
        
        for x1, y1 in neighbours:
            if int(grid[x1][y1]) - int(grid[x][y]) == 1:
                q.put((x1, y1))
    
    return count
            


with open("input.txt", 'r') as file:
    input = [line.strip('\n') for line in file.readlines()]
    
    grid = [['.'] + list(line) + ['.'] for line in input]
    grid.append(['.'] * len(grid[0]))
    grid.insert(0, ['.'] * len(grid[0]))
    
    zeros = find_zeros(grid)
    
    res = sum(calculate_score(grid, zero) for zero in zeros)
    
    print(res)
        
    

    