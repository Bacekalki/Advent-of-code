from functools import cache
import heapq
class Node:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
    
    def __lt__(self, other):
        return self.depth < other.depth
    
    def __repr__(self) -> str:
        return "(" + self.name + ", " + str(self.depth) + ")"


def calculate_depth(name, wires_dict, depth):
    if 'x' == name[0] or 'y' == name[0]:
        return depth
    
    return max(calculate_depth(wires_dict[name][0], wires_dict, depth + 1), calculate_depth(wires_dict[name][2], wires_dict, depth + 1))


def calc_values(values_dict, wires_dict, nodes_list):
    priority_queue = []
    for node in nodes_list:
        heapq.heappush(priority_queue, node)
    
    while len(priority_queue) > 0:
        current_node = heapq.heappop(priority_queue)
        args = wires_dict[current_node.name]
        
        arg1, operation, arg2 = args
        
        match operation:
            case 'AND':
                values_dict[current_node.name] = values_dict[arg1] & values_dict[arg2]
            
            case 'OR':
                values_dict[current_node.name] = values_dict[arg1] | values_dict[arg2]
            
            case 'XOR':
                values_dict[current_node.name] = values_dict[arg1] ^ values_dict[arg2]

def get_num(values_dict):
    my_list = [key for key in values_dict if key[0] == 'z']
    my_list.sort()
    num = [str(values_dict[key]) for key in my_list][::-1]
    
    return int(''.join(num), 2)

def get_involed(wire, wires_dict, res):
    if wire[0] == 'x' or wire[0] == 'y':
        res.append(wire)
        return

    get_involed(wires_dict[wire][0], wires_dict, res)
    get_involed(wires_dict[wire][2], wires_dict, res)
    
def get_suspects(wires_dict):
    sus = []
    for key in wires_dict:
        if key[0] == 'z' and not wires_dict[key][1] == 'XOR'and not key == 'z45':
            sus.append(key)
        
        if not key[0] == 'z' and wires_dict[key][1] == 'XOR' and wires_dict[key][0][0] not in 'xy' and not wires_dict[key][2][0] == 'xy':
            sus.append(key)
    
    return sus

def swap_output(first, second, wires_dict):
    wires_dict[first], wires_dict[second] = wires_dict[second], wires_dict[first]
    
def count_zeroes(str):
    return sum(1 for char in str if char == '0')
    
    
    

        

with open("input.txt", 'r') as file:
    lines = file.readlines()
    values_dict = {}
    switch = True
    wires_dict = {}
    nodes_list = []
    for line in lines:
        if line == '\n':
            switch = False
            continue
        if switch:
            splitted = line.strip('\n').split(' ')
            key = splitted[0][:-1:]
            values_dict[key] = int(splitted[1])
        else:
            splitted = line.strip('\n').split(' ')
            key = splitted[-1]
            wires_dict[key] = (splitted[0], splitted[1], splitted[2])
    
    swap_output('ckj', 'z15', wires_dict)
    swap_output('kdf', 'z23', wires_dict)
    swap_output('rpp', 'z39', wires_dict)
    # swap_output('vqr', 'jdk', wires_dict)
    
    
    for key in wires_dict:
        nodes_list.append(Node(key, calculate_depth(key, wires_dict, 0)))
        
    # print(get_suspects(wires_dict))
    
    print(','.join(sorted(['ckj', 'z15', 'kdf', 'z23', 'rpp', 'z39', 'fdv', 'dbp'])))
    
    # calc_values(values_dict, wires_dict, nodes_list)
    
    # my_str = ""
    # for key in values_dict:
    #     if key[0] == 'y':
    #         my_str = str(values_dict[key]) + my_str
    
    # print(my_str)
    
    
    # print(bin(get_num(values_dict) ^ (31016199577293 + 26066707720217)))
    
    
    
    
    

    