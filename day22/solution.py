import sys
from collections import defaultdict

def calculate(num, depth, previous, current_sequence, dp: dict[tuple, int]):
    if depth == 2000:
        return dp
    
    if len(current_sequence) == 4:
        my_tuple = tuple(current_sequence)
        if my_tuple not in dp:
            dp[my_tuple] = num % 10
        current_sequence.pop(0)
    
    
    
    res = num << 6
    num = res ^ num
    num = num & 0xFFFFFF
    new_res = num >> 5
    num = new_res ^ num
    num = num & 0xFFFFFF
    third_res = num << 11
    num = num ^ third_res
    num = num & 0xFFFFFF
    
    current_sequence.append(num % 10 - previous)
    
    
    
    return calculate(num, depth + 1, num % 10, current_sequence, dp)



with open("input.txt", 'r') as file:
    sys.setrecursionlimit(3000)
    nums = [int(line.strip('\n')) for line in file.readlines()]
    
    dps = [calculate(num, 0, num % 10, [], defaultdict(lambda: 0)) for num in nums]
    
    keys_set = set()
    max_sum = 0
    
    for dp in dps:
        keys_set.update(dp.keys())
    
    i = 0
    
    for key in keys_set:
        print(i)
        sum = 0
        for dp in dps:
            sum += dp[key]
        
        if sum > max_sum:
            max_sum = sum
        
        i += 1
    
    print('Found')
    print(max_sum)
        
    
    