def read_input() -> list[list[int]]:
    with open('input.txt', 'r') as file:
        data : list[list[int]] = []
        lines = file.readlines()
        for line in lines:
            nums : list[int] = list(map(int, list(line.strip())))
            data.append(nums)
        
        return data
    

def pick_digit(row : list[int], digit_index : int) -> tuple[list[int], int]:
    if digit_index == 0:
        candidates = row
    else:
        candidates = row[:-digit_index]
    digit = max(candidates)
    index = row.index(digit)
    return row[index + 1:], digit

def solve(data : list[list[int]]) -> int:
    total = 0
    for row in data:
        digits : list[int] = []
        new_row = row
        for i in range(11, -1, -1):
            new_row, digit = pick_digit(new_row, i)
            digits.append(digit)
        
        num = int("".join(list(map(str, digits))))
        total += num
    
    return total

if __name__ == "__main__":
    data = read_input()
    print(solve(data))
            
            