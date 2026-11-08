def get_type(list):
    type = ""
    if 1 <= list[0] - list[1] <= 3 and 1 <= list[1] - list[2] <= 3 and 1 <= list[2] - list[3] <= 3 and 1 <= list[3] - list[4] <= 3:
        type = 'decreasing'
    elif -3 <= list[0] - list[1] <= -1 and -3 <= list[1] - list[2] <= -1 and -3 <= list[2] - list[3] <= -1 and -3 <= list[3] - list[4] <= -1:
        type = 'increasing'
    
    return type


def eval_list(type, list, depth):
    if type == "" and depth == 1:
        return False
    elif type == "" and depth == 0:
        original_list = list.copy()
        original_list1 = list.copy()
        original_list2 = list.copy()
        original_list3 = list.copy()
        original_list4= list.copy()
        del original_list[0]
        del original_list1[1]
        del original_list2[2]
        del original_list3[3]
        del original_list4[4]
        return eval_list(get_type(original_list), original_list, 1) or eval_list(get_type(original_list1), original_list1, 1) or eval_list(get_type(original_list2), original_list2, 1) or eval_list(get_type(original_list3), original_list3, 1) or eval_list(get_type(original_list4), original_list4, 1)
    
    if type == 'increasing':
        for i in range(1, len(list) - 1) :
            if list[i] - list[i + 1] < -3 or list[i] - list[i + 1] > -1:
                original_list = list.copy()
                original_list1 = list.copy()
                del original_list[i]
                del original_list1[i + 1]
                if depth == 1:
                    return False
                else: 
                    return eval_list(get_type(original_list), original_list, 1) or eval_list(get_type(original_list1), original_list1, 1)
                
    else:
        for i in range(1, len(list) - 1) :
            if list[i] - list[i + 1] > 3 or list[i] - list[i + 1] < 1:
                
                original_list = list.copy()
                original_list1 = list.copy()
                del original_list[i]
                del original_list1[i + 1]
                if depth == 1:
                    return False
                else:
                    return eval_list(get_type(original_list), original_list, 1) or eval_list(get_type(original_list1), original_list1, 1)
            
    return True


with open("input.txt", 'r') as file:
    lines = file.readlines()
    input = [line.split(" ") for line in lines]
    converted_list = [[int(digit) for digit in sublist] for sublist in input]
    safe_counter = 0
    for list in converted_list:
        if eval_list(get_type(list), list, 0):
            safe_counter = safe_counter + 1
        
    
    
    print(safe_counter)