import os

def find_best_common_prefix(num_list, given_number):
    given_str = str(given_number)
    max_prefix_length = 0
    best_match = ""

    for num in num_list:
        num_str = str(num)
        common_length = 0

        # Compare characters to find the common prefix length
        for c1, c2 in zip(given_str, num_str):
            if c1 == c2:
                common_length += 1
            else:
                break
        
        # Update if this number has a longer common prefix
        if common_length > max_prefix_length:
            max_prefix_length = common_length
            best_match = num

    return best_match


    


def calculate_starting_values(num, dp):
    best_prefix = find_best_common_prefix(num, dp)
    if len(best_prefix) == 0:
        return {'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}, 0
    else:
        return dp[best_prefix], len(best_prefix)
            
        
    


def check_num(num, commands:list[(str, str, str)], inp_indexes, dp):
        
    values_dict, start_index = calculate_starting_values(num, dp)
    index = start_index
    
    if num == '45989929946998':
        print(values_dict)
        print('\n')
    
    current_number = ""
    
    
    for i in range(inp_indexes[start_index], len(commands)):    
        
        
        my_tuple = commands[i]
        command, first, second = my_tuple
        
        match command:
            case 'inp' :
                if i == 0:
                    current_number = num[:index + 1:]
                    values_dict['w'] = int(current_number[-1])
                else :
                    dp[current_number] = values_dict.copy()
                    # if num == '45989929946998':
                    #     print(current_number)
                    #     print(values_dict)
                    
                    index = index + 1
                    current_number = num[:index + 1:]
                    values_dict['w'] = int(current_number[-1])
                
                
                
            case 'add' :
                if second.isdigit() or second[0] == '-':
                    values_dict[first] = values_dict[first] + int(second)
                else :
                    values_dict[first] = values_dict[first] + values_dict[second]
                    
            case 'mul' :
                if second.isdigit() or second[0] == '-':
                    values_dict[first] = values_dict[first] * int(second)
                else :
                    values_dict[first] = values_dict[first] * values_dict[second]
                    
            case 'div' :
                if second.isdigit() or second[0] == '-':
                    values_dict[first] = values_dict[first] // int(second)
                else :
                    values_dict[first] = values_dict[first] // values_dict[second]
            
            case 'mod' :
                if second.isdigit() or second[0] == '-':
                    values_dict[first] = values_dict[first] % int(second)
                else :
                    values_dict[first] = values_dict[first] % values_dict[second]
            
            case 'eql' :
                if second.isdigit() or second[0] == '-':
                    values_dict[first] = 1 if values_dict[first] == int(second) else 0
                else :
                    values_dict[first] = 1 if values_dict[first] == values_dict[second] else 0    
        
    if values_dict['z'] == 0:
        print('Found it')
        print(num)
    else:
        return dp
        
def read_comands():
    with open("input.txt", 'r') as file:
        inp_indexes = []
        lines = file.readlines()
        commands = []
        index = 0
        for line in lines:
            new_line = line.strip()
            if line[:3:] == 'inp':
                inp_indexes.append(index)
            commands.append(new_line.split(" "))
            index = index + 1
        
        return commands, inp_indexes
    


commands, inp_indexes = read_comands()


dp = {}
ans = 45_989_929_946_199

for i in range(45_989_929_999_999, 45_000_000_000_000, -1):
    str_num = str(i)
    if '0' not in str_num:
        dp = check_num(str_num, commands, inp_indexes, dp)
    
    
    if i == ans - 1:
        print("Missed it")
        break       

        




    
        
    