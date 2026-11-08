def read_input() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return [list(line.strip()) for line in lines]


def solve(grid : list[list[str]]) -> int:
    first = grid[0]
    second = grid[1]
    index = first.index('S')
    second[index] = '|'
    total = 0
    
    for i in range(1, len(grid) - 1):
        current = grid[i]
        next = grid[i + 1]
        for j in range(len(current)):
            if current[j] == '|':
                if next[j] == '.' or next[j] == '|':
                    next[j] = '|'
                else:
                    next[j - 1] = '|'
                    next[j + 1] = '|'
                    total += 1
    
    return total

def pretty_print(grid : list[list[str]]):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    grid = read_input()
    print(solve(grid))
    
    