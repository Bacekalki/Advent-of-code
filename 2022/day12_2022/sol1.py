import heapq
def read_input() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return [list(line.strip('\n')) for line in lines]

def prepare_grid(grid : list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    S_coords = (0, 0)
    E_coords = (0, 0)
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == 'S':
                S_coords = (i, j)
            if char == 'E':
                E_coords = (i, j)
    x1, y1 = S_coords
    x2, y2 = E_coords
    grid[x1][y1] = 'a'
    grid[x2][y2] = 'z'
    return S_coords, E_coords
    
def get_neighbours(grid : list[list[str]], coords : tuple[int, int]) -> list[tuple[int, int]]:
    i, j = coords
    height = grid[i][j]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbours : list[tuple[int, int]] = []
    for dx, dy in directions:
        new_x, new_y = i + dx, j + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if ord(grid[new_x][new_y]) - ord(height) <= 1:
                neighbours.append((new_x, new_y))
    
    return neighbours

def manhattan_distance(coords1 : tuple[int, int], coords2 : tuple[int, int]) -> int:
    x1, y1 = coords1
    x2, y2 = coords2
    return abs(x1 - x2) + abs(y1 - y2)

def solve(grid : list[list[str]]):
    S_coords, E_coords = prepare_grid(grid)
    pq = [(manhattan_distance(S_coords, E_coords), S_coords, 0)]
    visited : set[tuple[int, int]] = set()
    distances = {S_coords : 0}
    
    while len(pq) > 0:
        _, current, moves_so_far = heapq.heappop(pq)
        
        if current == E_coords:
            return moves_so_far
        
        if current in visited:
            continue
        visited.add(current)
        
        neighbours = get_neighbours(grid, current)
        for neighbour in neighbours:
            if neighbour in distances:
                distances[neighbour] = min(moves_so_far, distances[neighbour])
            else:
                distances[neighbour] = moves_so_far
            
            heapq.heappush(pq, (manhattan_distance(neighbour, E_coords) + distances[neighbour], neighbour, moves_so_far + 1))
    
    
if __name__ == "__main__":
    grid = read_input()
    print(solve(grid))
        
        
    
            