def read_input() -> tuple[list[tuple[int, int]], list[int]]:
    ranges : list[tuple[int, int]] = []
    ids : list[int] = []
    
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        p = False
        for line in lines:
            line = line.strip()
            if line == "":
                p = True
                continue
            
            if not p:
                a, b = line.split('-')
                a, b = int(a), int(b)
                ranges.append((a, b))
            else:
                ids.append(int(line))
        
        return ranges, ids

def is_fresh(id : int, ranges : list[tuple[int, int]]) -> bool:
    for a, b in ranges:
        if a <= id <= b:
            return True
    
    return False

def solve(ranges : list[tuple[int, int]], ids : list[int]) -> int:
    return sum(1 for id in ids if is_fresh(id, ranges))

if __name__ == "__main__":
    ranges, ids = read_input()
    print(solve(ranges, ids))