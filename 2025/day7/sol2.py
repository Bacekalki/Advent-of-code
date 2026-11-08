def read_input() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]

def solve(grid : list[list[str]]) -> int:
    index = grid[0].index('S')
    grid[1][index] = '1'
    total = 0
    for i in range(1, len(grid) - 1):
        for j in range(len(grid[i])):
            if grid[i][j].isdecimal():
                if grid[i + 1][j] == '.':
                    grid[i + 1][j] = grid[i][j]
                elif grid[i + 1][j] == '^':
                    if grid[i + 1][j - 1].isdecimal():
                        grid[i + 1][j - 1] = str(int(grid[i + 1][j - 1]) + int(grid[i][j]))
                    else:
                        grid[i + 1][j - 1] = grid[i][j]
                    
                    if grid[i + 1][j + 1].isdecimal():
                        grid[i + 1][j + 1] = str(int(grid[i + 1][j + 1]) + int(grid[i][j]))
                    else:
                        grid[i + 1][j + 1] = grid[i][j]
                else:
                    grid[i + 1][j] = str(int(grid[i + 1][j]) + int(grid[i][j]))
    
    last = grid[-1]
    for cell in last:
        if cell.isdecimal():
            total += int(cell)
    
    return total

if __name__ == "__main__":
   grid = read_input()
   a = solve(grid)
   print(a)
   