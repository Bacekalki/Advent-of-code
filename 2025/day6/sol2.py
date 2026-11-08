import math
def read_input() -> list[str]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        return lines

def get_column(lines : list[str], i : int) -> list[str]:
    return [lines[row][i] for row in range(len(lines))]

def solve(lines : list[str]):
    columns = len(lines[0]) - 1
    current_sign = ''
    nums : list[int] = []
    total = 0
    
    for i in range(columns):
        column = get_column(lines, i)
        
        if all(char == ' ' for char in column):
            if current_sign == '+':
                total += sum(nums)
            else:
                total += math.prod(nums)
            nums.clear()
            continue
        
        num : list[str] = [] 
        if column[-1] != ' ':
            current_sign = column[-1]
            
        for char in column:
            if char.isdigit():
                num.append(char)
        
        current_num = int("".join(num))
        nums.append(current_num)
    
    if current_sign == '+':
        total += sum(nums)
    else:
        total += math.prod(nums)
    
    return total


if __name__ == "__main__":
   print(solve(read_input()))
        
        
