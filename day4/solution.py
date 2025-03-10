def check_for_xmas(grid, i, j):
    # left = ''.join([grid[i][j - index] for index in range(4)])
    # right = ''.join([grid[i][j + index] for index in range(4)])
    # up = ''.join([grid[i - index][j] for index in range(4)])
    # down = ''.join([grid[i + index][j] for index in range(4)])
    # up_left = ''.join([grid[i - index][j - index] for index in range(4)])
    # up_right = ''.join([grid[i - index][j + index] for index in range(4)])
    # down_right = ''.join([grid[i + index][j + index] for index in range(4)])
    # down_left = ''.join([grid[i + index][j - index] for index in range(4)])

    # my_list = [left, right, up, down, up_left, up_right, down_right, down_left]
    # return len([elem for elem in my_list if elem == "XMAS"])

    allowed_words = {"SAM", "MAS"}

    first_word = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
    second_word = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
    if first_word in allowed_words and second_word in allowed_words:
        return 1
    else:
        return 0


with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    new_grid = ['...' + line + '...' for line in lines]
    fill_str = '.' * (len(lines[0]) + 6)
    for i in range(0, 3):
        new_grid.insert(0, fill_str)
        new_grid.append(fill_str)
    
    xmas_counter = 0
    for i in range(3, len(new_grid) - 3):
        current_line = new_grid[i]
        for j in range(3, len(current_line) - 3):
            xmas_counter = xmas_counter + check_for_xmas(new_grid, i, j)

print(xmas_counter)