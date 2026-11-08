def read_input() -> list[tuple[int, int]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        points : list[tuple[int, int]] = []
        for line in lines:
            a, b = line.strip().split(',')
            points.append((int(a), int(b)))
        
        return points

def calculate_area(p1 : tuple[int, int], p2 : tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def solve(points : list[tuple[int, int]]) -> int:
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            current = calculate_area(points[i], points[j])
            if current > max_area:
                max_area = current
    
    return max_area


if __name__ == "__main__":
    print(solve(read_input()))
        