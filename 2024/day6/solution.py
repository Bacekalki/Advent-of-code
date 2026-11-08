
def find_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return i, j

def is_valid_position(map, pair):
     return 0 <= pair[0] < len(map) and 0 <= pair[1] < len(map[0])


def simulate_game_non_synchr(map, start_pos):
    if map is None:
        return 0

    directions = ["up", "right", "down", "left"]
    current = 0
    current_position = start_pos
    visited = set()

    while is_valid_position(map, current_position):
        
        current_direction = directions[current % 4]
        toAdd = (current_position[0], current_position[1])

        visited.add(toAdd)

        try:
            match current_direction:
                case "up":
                    if current_position[0] - 1 < 0:
                        return visited
                    if map[current_position[0] - 1][current_position[1]] == '#':
                        current += 1
                    else:
                        current_position = current_position[0] - 1, current_position[1]

                case "down":
                    if map[current_position[0] + 1][current_position[1]] == '#':
                        current += 1
                    else:
                        current_position = current_position[0] + 1, current_position[1]

                case "left":
                    if current_position[1] - 1 < 0:
                        return visited
                    if map[current_position[0]][current_position[1] - 1] == '#':
                        current += 1
                    else:
                        current_position = current_position[0], current_position[1] - 1

                case "right":
                    if map[current_position[0]][current_position[1] + 1] == '#':
                        current += 1
                    else:
                        current_position = current_position[0], current_position[1] + 1

        except IndexError:
            return visited
    
    return visited
    

def simulate_game(map, start_pos):
    if map is None:
        print("Finished")
        return

    directions = ["up", "right", "down", "left"]
    current = 0
    current_position = start_pos
    visited = set()

    while is_valid_position(map, current_position):
        current_direction = directions[current % 4]
        toAdd = (current_position[0], current_position[1], current_direction)

        
        if toAdd in visited:
            print("Finished")
            return 1
        else:
            visited.add(toAdd)

        try:
            match current_direction:
                case "up":
                    if current_position[0] - 1 < 0:
                        break
                    if map[current_position[0] - 1][current_position[1]] == '#':
                        current += 1
                    else:
                        current_position = current_position[0] - 1, current_position[1]

                case "down":
                    if map[current_position[0] + 1][current_position[1]] == '#':
                        current += 1
                    else:
                        current_position = current_position[0] + 1, current_position[1]

                case "left":
                    if current_position[1] - 1 < 0:
                        break
                    if map[current_position[0]][current_position[1] - 1] == '#':
                        current += 1
                    else:
                        current_position = current_position[0], current_position[1] - 1

                case "right":
                    if map[current_position[0]][current_position[1] + 1] == '#':
                        current += 1
                    else:
                        current_position = current_position[0], current_position[1] + 1

        except IndexError:
            return 0
    
    print("Finished")
    return 0
            

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        map = [[char for char in line.strip('\n')] for line in lines]
        
        start_pos = find_start(map)
        
        variants = simulate_game_non_synchr(map, start_pos)
        sum = 0
        
        for x, y in variants:
            if map[x][y] == '.':
                map[x][y] = '#'
                sum += simulate_game(map, start_pos)
                map[x][y] = '.'
        
        
        print(sum)
                
        
        
        
        