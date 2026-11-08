with open("input.txt", 'r') as input:
    lines = input.readlines()
    left_list = []
    right_list = []
    for line in lines:
        splitted = line.split("   ")
        left_list.append(int(splitted[0]))
        right_list.append(int(splitted[1]))
    
    zipped = zip(sorted(left_list), sorted(right_list))
    sum = 0
    
    for x, y in zipped:
        sum += abs(x - y)
    
    print(sum)
    