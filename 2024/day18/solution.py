import heapq
from queue import Queue

class Node():
    def __init__(self, location, price):
        self.location = location
        self.price = price
    
    def __lt__(self, other):
        return self.price < other.price


def generate_grid(width, height):
    grid = [['.' for i in range(width + 1)] for j in range(height + 1)]
    return grid

def get_neighbours(grid, current):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = current.location
    
    return [Node((x + dx, y + dy), current.price + 1) for dx, dy in directions if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx] == '.']

def find_cheapest(grid, start, end):
    priority_queue = []
    visited = set()
    s = Node(start, 0)
    visited.add(start)
    heapq.heappush(priority_queue, s)
    
    # print(get_neighbours(grid, s))
    
    while len(priority_queue) > 0:
        current = heapq.heappop(priority_queue)
        
        if current.location == end:
            return current.price

        neighbours = get_neighbours(grid, current)
        
        for neighbour in neighbours:
            if neighbour.location not in visited:
                visited.add(neighbour.location)
                heapq.heappush(priority_queue, neighbour)

def bfs(grid, start, end):
    q = Queue()
    visited = set()
    s = Node(start, 0)
    q.put(s)
    visited.add(start)
    
    while not q.empty():
        current = q.get()
        
        if current.location == end:
            return True
        
        neighbours = get_neighbours(grid, current)
        
        for neighbour in neighbours:
            if neighbour.location not in visited:
                visited.add(neighbour.location)
                q.put(neighbour)
    
    
    return False
    
    
    
    

with open("input.txt", 'r') as file:
    lines = file.readlines()
    corrupted = []
    for line in lines:
        splitted = line.strip('\n').split(',')
        corrupted.append((int(splitted[0]), int(splitted[1])))
    
    grid = generate_grid(70, 70)
    step = 0
    
    for x, y in corrupted:
        step += 1
        grid[y][x] = '#'
        if step == 1024:
            break
        
    counter = 0
    for x, y in corrupted:
        counter += 1
        if counter <= 1024:
            continue
        
        grid[y][x] = '#'
        
        if not bfs(grid, (0, 0), (70, 70)):
            print((x, y))
            break
    
        
        