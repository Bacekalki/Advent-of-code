import heapq
class Node():
    def __init__(self, location, direction, price = 0):
        self.location = location
        self.direction = direction
        self.price = price
    
    def __lt__(self, other):
        return self.price < other.price

def find_S_and_E(grid):
    start = (0, 0)
    end = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)

    return start, end


def get_opposite(direction):
    my_dict = {'>' : '<', '<': '>', 'v': '^', '^' : 'v'}
    return my_dict[direction]

def calculate_price(current_price, current_direction, other_direction):
    if other_direction == current_direction:
        return current_price + 1
    
    if other_direction == get_opposite(current_direction):
        return current_price + 2001
    
    return current_price + 1001

def is_part_of_optimal_path(grid, start, end, point):
    # price = find_cheapest_fake(grid, point, end) + find()
    pass
    # return price < 7036
    
    
    

def get_neighbours(grid, current):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    my_dict = {(0, 1) : '>', (1, 0): 'v', (-1, 0): '^', (0, -1) : '<'}
    x, y = current.location
    
    return [Node((x + dx, y + dy), my_dict[(dx, dy)], calculate_price(current.price, current.direction, my_dict[(dx, dy)])) for dx, dy in directions if not grid[x + dx][y + dy] == '#']
    
def get_neighbours_fake(grid, current):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    my_dict = {(0, 1) : '>', (1, 0): 'v', (-1, 0): '^', (0, -1) : '<'}
    x, y = current.location
    
    return [Node((x + dx, y + dy), my_dict[(dx, dy)], 1) for dx, dy in directions if not grid[x + dx][y + dy] == '#']

def find_cheapest(grid, start, end):
    priority_queue = []
    s = Node(start, '>', 0)
    heapq.heappush(priority_queue, s)
    visited = set()
    visited.add(s.location)
    
    while len(priority_queue) > 0:
        current = heapq.heappop(priority_queue)
        
        if current.location == end:
            # print('Here')
            return current.price, current.direction
        
        neighbours = get_neighbours(grid, current)
        
        for neighbour in neighbours:
            if neighbour.location not in visited:
                heapq.heappush(priority_queue, neighbour)
                visited.add(neighbour.location)
    
    return 999_999
    
    
    

def find_cheapest_fake(grid, start, direction, price, end, cheapest):
    priority_queue = []
    s = Node(start, direction, price)
    visited = set()
    visited.add(s.location)
    heapq.heappush(priority_queue, s)
    
    while len(priority_queue) > 0:
        current = heapq.heappop(priority_queue)
        
        if current.price > cheapest:
            return 999_999
        
        if current.location == end:
            # print('Here')
            return current.price
        
        neighbours = get_neighbours(grid, current)
        
        for neighbour in neighbours:
            if neighbour.location not in visited:
                heapq.heappush(priority_queue, neighbour)
                visited.add(neighbour.location)
    
    return 999_999



with open("input.txt", 'r') as file:
    lines = file.readlines()
    grid = [list(line.strip('\n')) for line in lines]
    
    cheapest = 83432
    
    # for line in grid:
    #     print(line)
    
    start, end = find_S_and_E(grid)
    sum = 0
    
    my_dict = {}
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j] == '#':
                print((i, j))
                my_dict[(i, j)] = find_cheapest(grid, start, (i, j))
    
    counter = 0
    for key in my_dict:
        print(key)
        price = find_cheapest_fake(grid, key, my_dict[key][1], my_dict[key][0], end, cheapest)
        if price == cheapest:
            counter += 1
    
    
    print(counter)
                
    
    
    # print(sum)
    
    
        
        


