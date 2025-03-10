def parse_line(line):
    splitted = line.split(' ')
    p = splitted[0][2::]
    v = splitted[1][2::]
    split_p = p.split(',')
    split_v = v.split(',')
    
    pair1 = int(split_p[0]), int(split_p[1])
    pair2 = int(split_v[0]), int(split_v[1])
    
    return pair1, pair2

def move(robot, grid_size):
    p, v = robot
    
    new_pos = (p[0] + v[0]) % grid_size[0], (p[1] + v[1]) % grid_size[1]
    
    return new_pos, v


def count_robots(robots, quadrant, grid_size):
    last_tile = (0, 0)
    first_tile = (0, 0)
    match quadrant:
        case 1:
            first_tile = 0, 0
            last_tile = (grid_size[0] - 1) // 2 - 1, (grid_size[1] - 1) // 2 - 1
        case 2:
            first_tile = (grid_size[0] - 1) // 2 + 1, 0
            last_tile = grid_size[0] - 1, (grid_size[1] - 1) // 2 - 1
        case 3:
            first_tile = 0, (grid_size[1] - 1) // 2 + 1
            last_tile = (grid_size[0] - 1) // 2 - 1, grid_size[1] - 1
        
        case 4:
            first_tile = (grid_size[0] - 1) // 2 + 1, (grid_size[1] - 1) // 2 + 1
            last_tile = grid_size[0] - 1, grid_size[1] - 1
    
    
    return sum(1 for p, _ in robots.values() if first_tile[0] <= p[0] <= last_tile[0] and first_tile[1] <= p[1] <= last_tile[1])


with open("input.txt", 'r') as file:
    lines = file.readlines()
    robots = {num: parse_line(line) for num, line in enumerate(lines)}
    grid_size = (101, 103)
    grid = [['.' for i in range(grid_size[0])] for j in range(grid_size[1])]
    
    second_list = []
    
    
    for second in range(0, 8258):
        for key, robot in robots.items():
            robots[key] = move(robot, grid_size)
            
        # prod = 1
        # for quadrant in range(1, 5):
        #     prod *= count_robots(robots, quadrant, grid_size)
            
        # second_list.append((second, prod))
        
        # if prod > max_prod:
        #     max_prod = prod
        #     min_sec = second
        
        if second == 8257:
            
            for p, _ in robots.values():
                grid[p[1]][p[0]] = '#'
        
            with open("tree.txt", 'a') as output:
                for line in grid:
                    output.write(''.join(line))
                    output.write('\n')
                output.write('\n')
    
    
    second_list.sort(key = lambda x: x[1])
    print(second_list[2])
        
    #print(min_sec)
    