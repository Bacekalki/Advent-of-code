import math
def read_input() -> tuple[list[list[int]], list[str]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        numbers : list[list[int]] = []
        for line in lines[:-1]:
            line = line.strip().split(' ')
            line = [num for num in line if num != '']
            numbers.append(list(map(int, line)))
        
        signs = lines[-1].strip().split(' ')
        signs = [sign for sign in signs if sign != '']
        return numbers, signs

def get_column(numbers : list[list[int]], i : int) -> list[int]:
    return[numbers[row][i] for row in range(len(numbers))]

def solve(numbers : list[list[int]], signs : list[str]) -> int:
    total = 0
    for i in range(len(signs)):
        col = get_column(numbers, i)
        sign = signs[i]
        if sign == "+":
            total += sum(col)
        else:
            total += math.prod(col)
    
    return total

if __name__ == "__main__":
    numbers, signs = read_input()
    print(solve(numbers, signs))
    