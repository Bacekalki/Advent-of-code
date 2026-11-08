def read_input() -> list[list[int]]:
    with open('input.txt', 'r') as file:
        data : list[list[int]] = []
        lines = file.readlines()
        for line in lines:
            nums : list[int] = list(map(int, list(line.strip())))
            data.append(nums)
        
        return data
    

def pick_first_digit(row : list[int]) -> tuple[list[int], int]:
    digit = max(row[:-1])
    index = row.index(digit)
    new_row = row[index + 1:]
    return new_row, digit



def solve(data : list[list[int]]) -> int:
    total = 0
    for row in data:
        new_row, first_digit = pick_first_digit(row)
        second_digit = max(new_row)
        total += (10 * first_digit + second_digit)
    
    return total

if __name__ == "__main__":
    data = read_input()
    print(solve(data))
        
        