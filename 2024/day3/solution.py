def check_command(temp: str, mul):
    splitted = temp.split(',')
    if not len(splitted) == 2:
        return 0
    if splitted[0].isdigit() and splitted[1].isdigit():
        print(mul + temp)
        return int(splitted[0]) * int(splitted[1])
    else:
        return 0


with open("input.txt", 'r') as file:
    lines = file.readlines()
    sum = 0
    is_enabled = True
    for line in lines:
        for i in range(len(line)):
            mul = line[i:i + 4]
            if mul == 'do()':
                is_enabled = True
                
            if mul == "don'":
                command = line[i:i + 7]
                if command == "don't()":
                    is_enabled = False

            if mul == "mul(" and is_enabled:
                k = i + 4
                temp = ""
                while not line[k] == ')':
                    temp += line[k]
                    k = k + 1

                sum += check_command(temp, mul)
    
    print(sum)
                