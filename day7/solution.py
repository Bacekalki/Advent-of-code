from collections import defaultdict

def appended(list, item):
    list.append(item)
    return list

def generate_series(chars, length, current_sol, solutions, stop_length):
    
    solutions[length].append(current_sol)
        
    if length == stop_length:
        return

    for char in chars:
        generate_series(chars, length + 1, appended(current_sol.copy(), char), solutions, stop_length)




def evaluate(target, nums, series):
    
    perms = series[len(nums) - 1]
    
    
    for perm in perms:
        
        current_res = nums[0]
        start_pos = 0
        
        for i in range(1, len(nums)):
            
            match perm[start_pos]:
                
                case '+':
                    current_res = current_res + nums[i]
                
                case '*':
                    current_res = current_res * nums[i]
                
                case '|':
                    current_res = int(str(current_res) + str(nums[i]))
            
            start_pos += 1
            
        if current_res == target:
            return target
    
    return 0

                
with open("input.txt", 'r') as file:
    # lines = file.readlines()
    
    # left_side = []
    # right_side = []
    
    # for line in lines:
    #     splitted = line.strip('\n').split(":")
    #     args = splitted[1].split(" ")
    #     my_list = [int(elem) for elem in args if elem.isdigit()]
    #     left_side.append(int(splitted[0]))
    #     right_side.append(my_list)
    
    # longest = max(len(v) for v in right_side)
    
    series = defaultdict(lambda: [])
    
    generate_series("+*", 0, [], series, 3)
    
    print(series)
    
    
    # sum = 0
    
    # for key, value in zip(left_side, right_side):
    #     print(key, value)
    #     sum += evaluate(key, value, series)
    
    
    # print("The final sum is")
    
    # print(sum)
   
    
    
    
    
        
    
    
    