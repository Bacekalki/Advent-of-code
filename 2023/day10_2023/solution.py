def getGrid() -> list[str]:
    with open('input.txt', 'r') as file:
       lines = [line.strip() for line in file]
       return lines


def findS(grid : list[str]) -> tuple[int, int]:
    for index, str in enumerate(grid):
        for j in range(len(str)):
            if grid[index][j] == 'S':
                return index, j
    
    return (0, 0)

def get_next(grid : list[str], x : int, y : int) -> list[tuple[int, int]]:
    current = grid[x][y]
    directions_dict = {'S' : [(1, 0), (-1, 0), (0, 1), (0, -1)], '-' : [(0, 1), (0, -1)], "|" : [(-1, 0), (1, 0)], "L" : [(-1, 0), (0, 1)], 
                       'J' : [(-1, 0), (0, -1)], '7' : [(1, 0), (0, -1)], 'F' : [(0, 1), (1, 0)]}
    
    return [(x + dx, y + dy) for dx, dy in directions_dict[current] if x + dx >= 0 and x + dx < len(grid) and y + dy >= 0 and y + dy < len(grid[0]) and not grid[x + dx][y + dy] == '.']

def find_furthest(grid : list[str]) -> int:
    x, y = findS(grid)
    visited : set[tuple[int, int]] = set()
    stack : list[tuple[int, int]] = []
    stack.append((x, y))
    visited.add((x, y))
    counter = 0
    
    while len(stack) > 0:
        curr_x, curr_y = stack.pop()
        neighbours = get_next(grid, curr_x, curr_y)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
        
        counter += 1
    
    return counter // 2

if __name__ == "__main__":
    grid = getGrid()
    print(find_furthest(grid))
        
        
        
    
    
        
        
        