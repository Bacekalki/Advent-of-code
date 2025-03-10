from collections import namedtuple

with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

garden = dict()
y_bound = len(lines)
x_bound = len(lines[0])
for y, this_line in enumerate(lines):
    for x, this_char in enumerate(this_line):
        garden[(x, y)] = this_char
to_be_visited = list(garden.keys())

Region = namedtuple('Region', ['coords', 'area', 'min_c', 'max_c'])


def flood_fill(start_coord: tuple, g_map: dict) -> list:
    # We will keep track of the x and y boundaries of this region to make the ray casting faster later on
    min_x, min_y = x_bound, y_bound
    max_x, max_y = 0, 0
    queue = [start_coord]  # queue keeps track of coordinates we have to check
    this_crop = g_map[start_coord]  # What letter crop are we even looking for
    this_region = set()  # Will keep all the unique coordinates in this region of this_crop
    checked = set()  # All the coordinates we've already checked
    while queue:  # Keep checking the queue while it isn't empty
        cx, cy = queue.pop()
        if g_map[(cx, cy)] == this_crop:
            # We've found this_crop, add it to this_region and update boundaries as needed
            this_region.add((cx, cy))
            if cx < min_x: min_x = cx
            if cy < min_y: min_y = cy
            if cx > max_x: max_x = cx
            if cy > max_y: max_y = cy
            # Now lets check all its neighbors
            for diff_coord in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = diff_coord
                # If it is in range and we haven't checked this neighbor already, add it to the queue
                if cx + dx in range(0, x_bound) and cy + dy in range(0, y_bound):
                    if (cx + dx, cy + dy) not in checked:
                        queue.append((cx + dx, cy + dy))
        checked.add((cx, cy))
    return [this_region, (min_x, min_y), (max_x, max_y)]


def ray_cast(this_region: set, mins: tuple, maxs: tuple) -> int:
    # We will draw horizontal lines and then vertical lines across the area where this_region is located
    # Every time we pass from outside the region to inside the region, or inside to outside, we've found a perimeter
    perimeter = 0
    minx, miny = mins
    maxx, maxy = maxs
    # Cast rays horizontally, counting every time we pass a boundary
    for this_y in range(miny, maxy + 1):
        in_bound = False  # Always start out of bounds
        for this_x in range(minx, maxx + 1):
            # If we've entered the region from outside
            if (this_x, this_y) in this_region and not in_bound:
                in_bound = True
                perimeter += 1
            # If we've exited the region
            elif (this_x, this_y) not in this_region and in_bound:
                in_bound = False
                perimeter += 1
        if in_bound:  # If we've reached the end of our checking zone and we are inside the region
            perimeter += 1

    # Do the same thing but vertically
    for this_x in range(minx, maxx + 1):
        in_bound = False
        for this_y in range(miny, maxy + 1):
            if (this_x, this_y) in this_region and not in_bound:
                in_bound = True
                perimeter += 1
            elif (this_x, this_y) not in this_region and in_bound:
                in_bound = False
                perimeter += 1
        if in_bound:
            perimeter += 1

    return perimeter


def count_corners(this_region: set) -> int:
    # Outside corners:
    # ?.   # If (x, y-1) (up) and (x-1, y) (left) are different from A
    # .A<  # Then A (with a caret pointed to it) is an outside corner

    # Inside corners:
    # VA   # if (x, y-1) and (x-1, y) are the same and (x-1, y-1) is different from A,
    # AA<  # then A (with a caret pointed to it) is an inside corner

    # Then check each rotation. A single coordinate can be a corner up to 4 times so we must check all ways.

    outside_check = [
        # different, different
        [(0, -1), (-1, 0)],
        [(0, -1), (1, 0)],
        [(1, 0), (0, 1)],
        [(-1, 0), (0, 1)]
    ]
    inside_check = [
        # Same, same, different
        [(0, -1), (-1, 0), (-1, -1)],
        [(0, -1), (1, 0), (1, -1)],
        [(1, 0), (0, 1), (1, 1)],
        [(-1, 0), (0, 1), (-1, 1)]
    ]
    corner_count = 0
    for coord in this_region:
        cx, cy = coord
        for o_coords in outside_check:
            ox1, oy1 = o_coords[0]
            ox2, oy2 = o_coords[1]
            if (cx + ox1, cy + oy1) not in this_region and (cx + ox2, cy + oy2) not in this_region:
                corner_count += 1
        for i_coords in inside_check:
            ox1, oy1 = i_coords[0]
            ox2, oy2 = i_coords[1]
            ox3, oy3 = i_coords[2]
            if ((cx + ox1, cy + oy1) in this_region and (cx + ox2, cy + oy2) in this_region and
                    (cx + ox3, cy + oy3) not in this_region):
                corner_count += 1
    return corner_count


regions = []
while to_be_visited:
    start_c = to_be_visited.pop()
    region_coords, min_coords, max_coords = flood_fill(start_c, garden)
    region_size = len(region_coords)
    regions.append(Region(region_coords, region_size, min_coords, max_coords))
    to_be_visited = list(set(to_be_visited).difference(region_coords))

cost = 0
cost2 = 0
for r in regions:
    for s in r.coords:
        perim = ray_cast(r.coords, r.min_c, r.max_c)
        corners = count_corners(r.coords)
        cost += r.area * perim
        cost2 += r.area * corners
        break

print(f"Part 1: {cost}")
print(f"Part 2: {cost2}")