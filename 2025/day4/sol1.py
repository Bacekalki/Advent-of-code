def read_input() -> list[str]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def get_neighbours(x : int, y : int, grid : list[str]) -> list[tuple[int, int]]:
    coords = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return [(x + dx, y + dy) for dx, dy in coords if x + dx >= 0 and y + dy >= 0 and x + dx < len(grid) and y + dy < len(grid[0])]

def solve(grid : list[str]) -> int:
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                neighbours = get_neighbours(i, j, grid)
                c = sum(1 for x, y in neighbours if grid[x][y] == '@')
                if c < 4:
                    total += 1
    
    return total

if __name__ == "__main__":
    print(solve(read_input()))