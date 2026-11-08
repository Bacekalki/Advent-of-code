def read_input() -> list[list[int]]:
    ranges : list[list[int]] = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
               ranges.sort(key = lambda x: x[0])
               return ranges

            a, b = line.split('-')
            ranges.append([int(a), int(b)])
    return []

def clean_ranges(ranges: list[list[int]]) -> list[list[int]]:
    if not ranges:
        return []
    
    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

def solve(ranges : list[list[int]]):
    ranges = clean_ranges(ranges)
    return sum(b - a + 1 for a, b in ranges)
        

if __name__ == "__main__":
    print(solve(read_input()))

            