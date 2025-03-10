import sys

def findS(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j


def get_neighbours(grid, point):
    x, y = point
    
    match grid[x][y]:
        case '-':
            return [(x, y - 1), (x, y + 1)]
        case '|':
            return [(x - 1, y), (x + 1, y)]
        case 'L':
            return [(x - 1, y), (x, y + 1)]
        case 'F':
            return [(x + 1, y), (x, y + 1)]
        case 'J':
            return [(x - 1, y), (x, y - 1)]
        case '7':
            return [(x + 1, y), (x, y - 1)]
        case '.':
            return []
        case 'S':
            list = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            return [elem for elem in list if point in get_neighbours(grid, elem)]

def dfs(grid, current_point, step, visited, lengths):
    
    a, b = current_point
    if grid[a][b] == 'S' and step > 0:
        lengths.append(step)
        return 
    
    neighbours = get_neighbours(grid, current_point)
    
    if (current_point == (58, 100)):
        print("Yes")
        print(step)
    
    print(step)
    
    for x, y in neighbours:
        if grid[x][y] == 'S':
            if step > 1:
                dfs(grid, (x, y), step + 1, visited | {(x, y)}, lengths)
        
        if (x, y) not in visited:
            if current_point == (58, 101):
                print('Here')
                print(grid[58][101])
                print((x, y))
            dfs(grid, (x, y), step + 1, visited | {(x, y)}, lengths)
     
                
with open("input.txt", 'r') as file:
    sys.setrecursionlimit(10**6)
    
    input = file.readlines()
    input = [list(line.strip('\n')) for line in input]

    grid = [['.'] + line + ['.'] for line in input]

    grid.append(['.'] * len(grid[0]))
    grid.insert(0, ['.'] * len(grid[0]))
    
    # for i in range(len(grid)):
    #     if 57 <= i <= 59:
    #         print(grid[i][100:111])

    start = findS(grid)
    
    print(start)


    lengths = []

    dfs(grid, start, 0, set(), lengths)

    print(lengths)


    print(max(lengths) // 2)



