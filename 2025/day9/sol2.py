def read_input() -> list[tuple[int, int]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        points : list[tuple[int, int]] = []
        for line in lines:
            a, b = line.strip().split(',')
            points.append((int(a), int(b)))
        
        return points

def connect_red_tiles(red_tiles : list[tuple[int, int]]) -> set[tuple[int, int]]:
    green_tiles : set[tuple[int, int]] = set()
    for i in range(len(red_tiles) - 1):
        current, next = red_tiles[i], red_tiles[i + 1]
        if current[0] == next[0]:
            max_y = max(current[1], next[1])
            min_y = min(current[1], next[1])
            for j in range(min_y + 1, max_y):
                green_tiles.add((current[0], j))
        else:
            max_x = max(current[0], next[0])
            min_x = min(current[0], next[0])
            for j in range(min_x + 1, max_x):
                green_tiles.add((j, current[1]))
    
    last = red_tiles[-1]
    first = red_tiles[0]
    if first[0] == last[0]:
        max_y = max(first[1], last[1])
        min_y = min(first[1], last[1])
        for j in range(min_y + 1, max_y):
            green_tiles.add((first[0], j))
    else:
        max_x = max(first[0], last[0])
        min_x = min(first[0], last[0])
        for j in range(min_x + 1, max_x):
            green_tiles.add((j, first[1]))
    
    return green_tiles


def calculate_area(p1 : tuple[int, int], p2 : tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def get_all_rectangles(red_points : list[tuple[int, int]]):
    rectangles : list[tuple[tuple[int,int], tuple[int,int], int]] = []
    for i in range(len(red_points)):
        for j in range(i + 1, len(red_points)):
            rectangles.append((red_points[i], red_points[j], calculate_area(red_points[i], red_points[j])))
    
    rectangles.sort(key = lambda x: -x[2])
    return rectangles

def is_inside_rectangle(p1 : tuple[int, int], p2 : tuple[int, int], point : tuple[int, int]):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = point
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    return (min_x < x3 < max_x and min_y < y3 < max_y)
    

def is_rectangle_valid(p1 : tuple[int, int], p2 : tuple[int, int], point_set : set[tuple[int, int]]):
    return not any(is_inside_rectangle(p1, p2, x) for x in point_set)


def solve(red_points : list[tuple[int, int]]):
    rectangles = get_all_rectangles(red_points)
    green_points = connect_red_tiles(red_points)
    union = green_points.union(red_points)
    
    for p1, p2, area in rectangles:
        if is_rectangle_valid(p1, p2, union):
           return p1, p2, area


if __name__ == "__main__":
    print(solve(read_input()))



    