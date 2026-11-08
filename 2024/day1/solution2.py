from collections import Counter
with open("input.txt", 'r') as input:
    lines = input.readlines()
    left_list = []
    right_list = []
    for line in lines:
        splitted = line.split("   ")
        left_list.append(int(splitted[0]))
        right_list.append(int(splitted[1]))
    
    right_counter = Counter(right_list)
    sum = 0
    for left in left_list:
        sum += left * right_counter[left]
    
    print(sum)
    