from queue import Queue
from itertools import combinations


def count_diagonal(point1, point2, grid):
    neighbours1 = get_neigbours(grid, point1)
    neighbours2 = get_neigbours(grid, point2)
    
    
    good_neighbours1 = [(x, y) for x, y in neighbours1 if grid[x][y] == grid[point1[0]][point1[1]]]
    good_neighbours2 = [(x, y) for x, y in neighbours2 if grid[x][y] == grid[point2[0]][point2[1]]]
    
    bad_neighbours1 = [(x, y) for x, y in neighbours1 if not grid[x][y] == grid[point1[0]][point1[1]]]
    bad_neighbours2 = [(x, y) for x, y in neighbours2 if not grid[x][y] == grid[point2[0]][point2[1]]]
    
    if len (bad_neighbours1) == 1 and len(bad_neighbours2) == 1:
        if set(bad_neighbours1) == set(bad_neighbours2):
            return 1
        
    if len(set(bad_neighbours1).intersection(set(bad_neighbours2))) > 1:
        #print(0)
        return 0
    
    if len (bad_neighbours1) == 3 and len(bad_neighbours2) == 3:
        return 1
    
    
    
    if len(set(good_neighbours1).intersection(set(good_neighbours2))) > 1:
        #print(0)
        return 0
    
    
    
    # print(point1)
    # print(point2)
    # print(1)
    return 1
    
    
    
    
    
    

class Shape:
    grid = []
    
    def __init__(self, points):
        self.points = points
        self.plant = grid[points[0][0]][points[0][1]]
    
    
    def __repr__(self):
        return str(self.points)
    
    def get_area(self):
        return len(self.points)
    
    
    def evaluate_sides(self):
        if len(self.points) == 1:
            return 4
        
        ones_doubles_triples = []
        
        sides = 0
        
        for point in self.points:
            neighbours = get_neigbours(grid, point)
            my_list = [(x, y) for x, y in neighbours if not grid[x][y] == self.plant]
            count = len(my_list)
            if count == 3:
                #print(point)
                sides = sides + 2
                ones_doubles_triples.append(point)
                
            if count == 2:
                ones_doubles_triples.append(point)
                pair1, pair2 = my_list
                
                x1, y1 = pair1
                x2, y2 = pair2
                
                diff = (abs(x1 - x2), abs(y1 - y2))
                
                if diff == (1, 1):
                    # print(point)
                    sides = sides + 1
            
            if count == 1:
                ones_doubles_triples.append(point)
        
        print(sides)
        
        
        combs = list(combinations(ones_doubles_triples, 2))
        for first, second in combs:
            diff = (abs(first[0] - second[0]), abs(first[1] - second[1]))
            
            if diff == (1, 1):
                #print(count_diagonal(first, second, grid))
                sides += count_diagonal(first, second, grid)
        
        
        return sides
            
       
            
        
        
                     
                
def get_neigbours(grid, point):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = point
    return [(x + dx, y + dy) for dx, dy in directions]



def bfs(grid, start, visited):
    x, y = start
    visited[x][y] = True
    q = Queue()
    q.put(start)
    points = [start]
    
    while not q.empty():
        current = q.get()
        neighbours = get_neigbours(grid, current)
       
        for x1, y1 in neighbours:
            if not grid[x1][y1] == '.' and not visited[x1][y1] and grid[x][y] == grid[x1][y1]:
                q.put((x1, y1))
                visited[x1][y1] = True
                points.append((x1, y1))
    
    
    
    return Shape(points)
        
    


with open("input.txt", 'r') as file:
    input = file.readlines()
    
    grid = [['.'] + list(line.strip('\n')) + ['.'] for line in input]
    grid.append(['.'] * len(grid[0]))
    grid.insert(0, ['.'] * len(grid[0]))
    Shape.grid = grid
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    
    my_shapes = []
    
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if not visited[i][j]:
                my_shapes.append(bfs(grid, (i, j), visited))

    my_sum = 0
    for shape in my_shapes:
        #print(shape)
        sides = shape.evaluate_sides()
        #print(sides if sides % 2 == 0 else sides + 1)
        my_sum += (shape.get_area() * (sides if sides % 2 == 0 else sides + 1))
        
    
    print(my_sum)
    
    
    
    
    
                
    
    