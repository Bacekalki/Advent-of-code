def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j

def appended(list, pair):
    list.append(pair)
    return list


def sum_all_boxes(grid):
    my_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                my_sum += 100 * i + j
                
    return my_sum
    

def is_move_valid(grid, position, direction):
    x, y = position
    my_stack = []
    stack_to_return = []
    visited = set()
    if direction == '^':
        my_stack.append(position)
        stack_to_return.append(position)
        visited.add(position)
        my_stack.append((x - 1, y))
        stack_to_return.append((x - 1, y))
        visited.add((x - 1, y))
        if grid[x - 1][y] == '[':
            my_stack.append((x - 1, y + 1))
            stack_to_return.append((x - 1, y + 1))
            visited.add((x - 1, y + 1))
        if grid[x - 1][y] == ']':
            my_stack.append((x - 1, y - 1))
            stack_to_return.append((x - 1, y - 1))
            visited.add((x - 1, y - 1))
        while len(my_stack) > 0:
            x1, y1 = my_stack.pop()
            
            if grid[x1 - 1][y1] == '#':
                return False, []
            
            if grid[x1 - 1][y1] == '[':
                
                if (x1 - 1, y1 + 1) not in visited:
                    my_stack.append((x1 - 1, y1 + 1))
                    stack_to_return.append((x1 - 1, y1 + 1))
                    visited.add((x1 - 1, y1 + 1))
                  
                if (x1 - 1, y1) not in visited:  
                    my_stack.append((x1 - 1, y1))
                    visited.add((x1 - 1, y1))
                    stack_to_return.append((x1 - 1, y1))
            
            if grid[x1 - 1][y1] == ']':
                if (x1 - 1, y1 - 1) not in visited:
                    my_stack.append((x1 - 1, y1 - 1)) 
                    visited.add((x1 - 1, y1 - 1))
                    stack_to_return.append((x1 - 1, y1 - 1))
                    
                if (x1 - 1, y1) not in visited: 
                    my_stack.append((x1 - 1, y1))
                    visited.add((x1 - 1, y1)) 
                    stack_to_return.append((x1 - 1, y1))
                 
        
        return True, stack_to_return        
    
    else:
            my_stack.append(position)
            stack_to_return.append(position)
            visited.add(position)
            my_stack.append((x + 1, y))
            visited.add((x + 1, y))
            stack_to_return.append((x + 1, y))
            if grid[x + 1][y] == '[':
                my_stack.append((x + 1, y + 1))
                stack_to_return.append((x + 1, y + 1))
                visited.add((x + 1, y + 1))
            if grid[x + 1][y] == ']':
                my_stack.append((x + 1, y - 1))
                stack_to_return.append((x + 1, y - 1))
                visited.add((x + 1, y - 1))
            while len(my_stack) > 0:
                x1, y1 = my_stack.pop()
                
                if grid[x1 + 1][y1] == '#':
                    return False,[]
                
                if grid[x1 + 1][y1] == '[':
                    if (x1 + 1, y1 + 1) not in visited:
                        my_stack.append((x1 + 1, y1 + 1))
                        visited.add((x1 + 1, y1 + 1))
                        stack_to_return.append((x1 + 1, y1 + 1))
                    
                    if (x1 + 1, y1) not in visited:
                        my_stack.append((x1 + 1, y1))    
                        visited.add((x1 + 1, y1))
                        stack_to_return.append((x1 + 1, y1))
                
                
                if grid[x1 + 1][y1] == ']':
                    if (x1 + 1, y1 - 1) not in visited:
                        my_stack.append((x1 + 1, y1 - 1))
                        visited.add((x1 + 1, y1 - 1))
                        stack_to_return.append((x1 + 1, y1 - 1))
                    
                    if (x1 + 1, y1) not in visited:
                        my_stack.append((x1 + 1, y1))   
                        visited.add((x1 + 1, y1))
                        stack_to_return.append((x1 + 1, y1))
                    
            
            return True, stack_to_return
         
            
            
def swap_positions(grid, first, second):
    x, y = first
    x1, y1 = second
    
    grid[x][y], grid[x1][y1] = grid[x1][y1], grid[x][y]
    
            
def move(grid, current_pos, direction, swaps):
    dir = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v' : (1, 0)}
    x, y = current_pos
    dx, dy = dir[direction]
    
    if grid[x + dx][y + dy] == '.':
        swaps.append(((x,y), (x + dx, y + dy)))
        for swap in swaps[::-1]:
            swap_positions(grid, swap[0], swap[1])
            
        return swaps[0][1]
    
    if grid[x + dx][y + dy] == '#':
        if len(swaps) == 0:
            return current_pos
        else:
            return swaps[0][0]
    
    if (grid[x + dx][y + dy] == '[' or grid[x + dx][y + dy] == ']') and (direction == '>' or direction == '<'):
        return move(grid, (x + dx, y + dy), direction, appended(swaps, (current_pos, (x + dx, y + dy))))
    
    if (grid[x + dx][y + dy] == '[' or grid[x + dx][y + dy] == ']') and (direction == '^' or direction == 'v'):
        res = is_move_valid(grid, current_pos, direction)
        if res[0]:
            my_list = res[1]
            # print(my_list)
            if direction == '^':
                my_list = sorted(my_list, key = lambda x: x[0], reverse = True)
                for x1, y1 in my_list[::-1]:
                    swap_positions(grid, (x1, y1), (x1 - 1, y1))
                    
                return current_pos[0] - 1, current_pos[1]
            else:
                my_list = sorted(my_list, key = lambda x: x[0])
                for x1, y1 in my_list[::-1]:
                    swap_positions(grid, (x1, y1), (x1 + 1, y1))
                
                return current_pos[0] + 1, current_pos[1]
        else:
            return current_pos


def generate_new_grid(grid):
    new_grid = []
    for line in grid:
        new_line = []
        for char in line:
            if char == '#' or char == '.':
                new_line.append(char)
                new_line.append(char)
            
            if char == '@':
                new_line.append('@')
                new_line.append('.')
            
            if char == 'O':
                new_line.append('[')
                new_line.append(']')
        
        new_grid.append(new_line)
    
    return new_grid
                
                



with open("grid.txt", 'r') as grid_file:
    with open("moves.txt", 'r') as moves_file:
        grid = grid_file.readlines()
        moves = moves_file.readlines()
        grid = [list(line.strip('\n')) for line in grid]
        grid = generate_new_grid(grid)
        moves_str = ""
        for line in moves:
            moves_str += line.strip('\n')
            
        
        # for line in grid:
        #     print(line)
        
        
        # print('\n')
        
        
        start = find_robot(grid)
        index = 0
        
        for char in moves_str:
            start = move(grid, start, char, [])
            index += 1
        
            # for line in grid:
            #     print(line)
        
            # print(char)
            # print('\n')
        
        print(sum_all_boxes(grid))
        
        
        
        
    