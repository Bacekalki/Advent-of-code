def read_input() -> list[tuple[int, int]]:
    data : list[tuple[int, int]] = []
    with open('input.txt', 'r') as file:
        line = file.readline()
        ranges = line.strip().split(',')
        for range in ranges:
            a, b = range.split('-')
            a, b = int(a), int(b)
            data.append((a, b))

        return data
    


def is_num_wrong(num : int) -> bool:
    str_num = str(num)
    n = len(str_num)
    for i in range(1, n // 2 + 1):
        splitted = split_num(str_num, i)
        if len(set(splitted)) == 1:
            return True
    
    return False
        
        

def split_num(num : str, i : int) -> list[str]:
    return [num[start:start + i] for start in range(0, len(num), i)]
        
def solve(data : list[tuple[int, int]]) -> int:
    total = 0
    for a, b in data:
        for i in range(a, b + 1):
            if is_num_wrong(i):
                total += i
    
    return total

if __name__ == "__main__":
    print(solve(read_input()))