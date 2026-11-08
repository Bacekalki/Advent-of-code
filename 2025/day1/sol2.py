def read_data() -> list[tuple[str, int]]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        instructions : list[tuple[str, int]] = []
        for line in lines:
            line = line.strip()
            direction, value = line[0], int(line[1:])
            instructions.append((direction, value))
        
        return instructions

def solve(instructions : list[tuple[str, int]]):
    current = 50
    counter = 0
    for direction, value in instructions:
        if direction == "R":
            new_val = current + value
            counter += new_val // 100
            current = new_val % 100
        else:
            new_val = current - value
            counter += abs(new_val // 100)
            if current == 0 and new_val % 100 > 0:
                counter -= 1
            elif current > 0 and new_val % 100 == 0:
                counter += 1
            current = new_val % 100
            
    return counter

if __name__ == "__main__":
    instructions = read_data()
    print(solve(instructions))