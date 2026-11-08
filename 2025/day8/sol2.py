import math
def read_input() -> list[tuple[int, int, int]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        points : list[tuple[int, int, int]] = []
        for line in lines:
            a, b, c = list(map(int, line.strip().split(',')))
            points.append((a, b, c))
        
        return points

def euclidean_distance(a : tuple[int, int, int], b : tuple[int, int, int]) -> float:
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))
    

def sort_points(points : list[tuple[int, int, int]]) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    pairs : list[tuple[tuple[int, int, int], tuple[int, int, int], float]] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs.append((points[i], points[j], euclidean_distance(points[i], points[j])))
    
    pairs.sort(key = lambda x: x[2])
    return [(a, b) for a, b, _ in pairs]

def solve(points : list[tuple[int, int, int]]) -> int:
    pairs = sort_points(points)
    points_dict = {point : index for index, point in enumerate(points)}
    
    for pair in pairs:
        a, b = pair
        circ_a = points_dict[a]
        circ_b = points_dict[b]
        
        if circ_a == circ_b:
            continue
        
        min_circ = min(circ_a, circ_b)
        max_circ = max(circ_a, circ_b)
        
        for key in points_dict:
            if points_dict[key] == max_circ:
                points_dict[key] = min_circ
    
        if all(index == 0 for index in points_dict.values()):
            return a[0] * b[0]
        
    

if __name__ == "__main__":
    print(solve(read_input()))