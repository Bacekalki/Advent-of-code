import math

class Operation:
    def __init__(self, name, args = "", type = ""):
        self.name = name
        self.args = args
        self.type = type
    
    def __repr__(self):
        return "Operation(" + self.name + ", " + str(self.args) + ", " + self.type  + ")"

class Literal_value:
    def __init__(self, num, length):
        self.num = num
        self.length = length
    
    def __repr__(self):
        return "Literal_value(" + str(self.num) + ", " + str(self.length) + ")"
     


def get_version(packet):
    return int(packet[:3], 2)

def get_type(packet):
    return int(packet[3:6], 2)

def get_length(packet):
    return packet[6]

def get_length_of_subpackets(packet):
    return int(packet[7:22], 2)

def get_num_of_subpackets(packet):
    return int(packet[7:18], 2)

def parse_literal_value(packet):
    i = 0
    number = ""
    gr = ""
    
    while True:
        group = packet[i:i + 5]
        number += group[1::]
        gr += group
        if group[0] == '0':
            
            return i + 5, int(number, 2), len(gr)
        
        else:
            i = i + 5

    
    
        

def decode(packet, operations_list, operations_dict):
    
    if len(packet) < 11:
        return
    
    op = Operation(operations_dict[int(get_type(packet))])
    
    
    if get_type(packet) == 4:
        index, number, length = parse_literal_value(packet[6::])
        operations_list.append(Literal_value(number, length + 6))
        decode(packet[index+ 6::], operations_list, operations_dict)
    
    else:
        length_id = get_length(packet)
        if length_id == '0':
            length = get_length_of_subpackets(packet)
            op.args = length
            op.type = "length_in_bits"
            operations_list.append(op)
            decode(packet[22::], operations_list, operations_dict)
        
        else:
            number_of_subpackets = get_num_of_subpackets(packet)
            op.args = number_of_subpackets
            op.type = "count_of_args"
            operations_list.append(op)
            decode(packet[18::], operations_list, operations_dict)


def evaluate_expr(operations_list):
    
    args = []
    counter = 0
    
    for operation in operations_list[::-1]:
        
        bits = 0
        
        # counter += 1
        
        # if counter == 5:
        #     break
        
        if isinstance(operation, Literal_value):
            args.append(operation)
        
        else:
            
            match operation.name:
                case "sum":
                    type = operation.type
                    params = operation.args
                    my_sum = 0
                    if type == "count_of_args":
                        bits = 18
                        my_sum = sum([val.num for val in args[-params:]])
                        lens = [val.length for val in args[-params:]]
                        args = args[:-params]
                        
                    else:
                        current_len = 0
                        my_list = []
                        lens = []
                        bits = 22
                        for arg in args[::-1]:
                            current_len += arg.length
                            my_list.append(arg.num)
                            lens.append(arg.length)
                            if current_len >= params:
                                break
                        
                        my_sum = sum(my_list)
                        args = args[:-len(my_list)]
                    
                    args.append(Literal_value(my_sum, sum(lens) + bits))
                    
                
                case "product":
                    type = operation.type
                    params = operation.args
                    my_product = 1
                    if type == "count_of_args":
                        bits = 18
                        my_product = math.prod([val.num for val in args[-params:]])
                        lens = [val.length for val in args[-params:]]
                        args = args[:-params]
                        
                    else:
                        current_len = 0
                        my_list = []
                        lens = []
                        bits = 22
                        for arg in args[::-1]:
                            current_len += arg.length
                            my_list.append(arg.num)
                            lens.append(arg.length)
                            if current_len >= params:
                                break
                        
                        my_product = math.prod(my_list)
                        args = args[:-len(my_list)]
                    
                    args.append(Literal_value(my_product, sum(lens) + bits))
                
                case "min":
                    type = operation.type
                    params = operation.args
                    my_min = 1
                    if type == "count_of_args":
                        bits = 18
                        my_min = min([val.num for val in args[-params:]])
                        lens = [val.length for val in args[-params:]]
                        args = args[:-params]
                        
                    else:
                        current_len = 0
                        my_list = []
                        lens = []
                        bits = 22
                        for arg in args[::-1]:
                            current_len += arg.length
                            my_list.append(arg.num)
                            lens.append(arg.length)
                            if current_len >= params:
                                break
                        
                        my_min = min(my_list)
                        args = args[:-len(my_list)]
                    
                    args.append(Literal_value(my_min, sum(lens) + bits))
                
                case "max":
                    type = operation.type
                    params = operation.args
                    my_max = 1
                    if type == "count_of_args":
                        bits = 18
                        my_max = max([val.num for val in args[-params:]])
                        lens = [val.length for val in args[-params:]]
                        args = args[:-params]
                        
                    else:
                        current_len = 0
                        my_list = []
                        lens = []
                        bits = 22
                        for arg in args[::-1]:
                            current_len += arg.length
                            my_list.append(arg.num)
                            lens.append(arg.length)
                            if current_len >= params:
                                break
                        
                        my_max = max(my_list)
                        args = args[:-len(my_list)]
                    
                    args.append(Literal_value(my_max, sum(lens) + bits))
                    
                case ">":
                    bits = 18 if operation.type == "count_of_args" else 22
                    result = 1 if args[-1].num > args[-2].num else 0
                    lens = args[-1].length + args[-2].length
                    args = args[:-2]
                    args.append(Literal_value(result, lens + bits))
                
                case "<":
                    bits = 18 if operation.type == "count_of_args" else 22
                    result = 1 if args[-1].num < args[-2].num else 0
                    lens = args[-1].length + args[-2].length
                    args = args[:-2]
                    args.append(Literal_value(result, lens + bits))
                
                case "=":
                    bits = 18 if operation.type == "count_of_args" else 22
                    result = 1 if args[-1].num == args[-2].num else 0
                    lens = args[-1].length + args[-2].length
                    args = args[:-2]
                    args.append(Literal_value(result, lens + bits))
            
        # for arg in args:
        #     print(arg)
        
        # print("End")
    
    return args
            
            
            
                    
        
        

with open("input.txt", 'r') as file:
    packet = '0110000001010011001000110001000000000100110000010010110111000010011011010000000001010010011010111110111001110010100011010010110000000001001110101100011101111001010110101100101001110101011011111001001110110101001001001101100000000000000010101010110010001111111110000000101100111010011110100100000000010110111101101000000000101101001101011100011111001001010011001000101011001001011110101101100000011101001100000000001001001100000000001101000100000000001111001000000010101101000001010000000000101001110000000000111000100000001001000000010110000000100001010011010000000001111010011000110000000000110101010000000000111000010000000000110101000000000101010001100011000000000011000111000000000011100010000000001101110110001100000000001010010000000000100011000000000000000001100000110110000000000011010000100110111001110100000011111001111111010101000110100100110000000001010010110000000001011000000000000001000010001000100011010000100000100011001100000000000000100001010100011101111000110011110000111010100111110010011100100000000010101011001110000000000101111111100100111010111110000110111001100111101010010011001000101000101010100000000100110100100110011100110000111000100101101010101000101100100011110010111101111001111100100001010101100000001000000001010111110010011100100001110111000110001101111111101110110110011010000000001000100010000000001110010001010100100000101111000010100000000000000001000010011000001100010001001100100011100100011000000000100001101000000000100110000000000000100001111100010101001000010000110000101001000100000000011011100011001001000110101110001101110100100111001111100111001110111111110000101010001100000000000100000101001001100011110001100000000101001100101010100101110010100010000001001110100000000100100010011000010011011001111001001100011111111101000011111010010000010000000001100100011111000000000010101001010011100111010111101010011100111010111111110011110111101100111101111000110110110010100101011010111100010100000110000000000101111011100110001110010011101000001010110010101010100110010000000000110000101100111110001010010011010010000111001101001011110000100000000011011001100000000011100100001001011000001011110001110010001100000000011101100001010011000110000110001101110001100000000011010100001001101000101011010001011010001100000000100110100011101101001011001011011100101110000010010011010000010000010000000001100000011101100000000010101100101000010110010011011110100111001110011010110011001110111111111110100111110100101101101101001100001000000000101101110010010100100000000011110110000000001010010010101101010011100010011101111111101011001010100100010000000000100000011100111000001111110011101001010100010000000001011010110110000000000011010000010010111111001001101011001100101111110010011010111111001111100011010010100000000101100100101101011001011011100111001110011001111101110011101111001000001100010100110000111000010011101101111111011001111111100011111011000101000000110100100000000011100110011001110011101110100100010111000000000010000110001001100010111110111011000010000100111101011011111100111000000110010001100000000001011100100010000111100100000000100100011101001110111110000110001010000000001100110011000100000000011000100010111111000011011110000100010000100000000011011100011010101000100101010000011001010000000000000101110010000010011100110001001100111010001100000000010001100101101001111010111011000000100010110000000000010000001110010010010100111001001001010111010100000000011111100110001100110001000001011001001011101010011101000111100000110000000001010010100000000001110010011001110010011100101100100001010100111001011111110011101011001111100101111100111111100100000111001000000000101101101111010000000001000010010001001100011001111011000110001001111000111011110001000101100001001110001000000001001111000001111110010001101100001011110011010110000010101010000101101001000000000110000000110110000000001001010011110110101001110000101101111111110001111101001101001010010100101100101110101110000000010001110010110110101000010111010100001001111110001101111101100001111100111011010011101101010001101010011010000011111001101011110100100101100000010000000001100110011111101010010010110001101001100010000100010000000001101010110100110110011111010110000000001010110010111101011000011111110100010000110010111101011000011111110100010010100100000000001111011001011000000000101101000110000010001100100100110001110101010100011100000000101010100110111000101001001100101101001111001011101101000101001110011001101001001001111001100110111001100100000100100111010010101110010000000100000000000011100110111000101111010010110010010011001100010011011111111001010110100100101001110110110011111011101011100001001000100111000001000000001001101110011100000000011001100010001000000000110101000011010110000101001100001101010001000000000111111000101011010000011100100010110111001110110000110001001001001110100100101011011000111001110011000101101011110100000100110011000000000111000000000000000100001101100011110011000011111110000110111000000000000010000101010000011010100011001111000011111100010000000001111010001100010100001101001000110111000000000000000010111011000100110110011100111100110110001010000000001000010011100100111000111101100100100010010010010110111101111000010011010010000000001111001011100110111101011010111111001110111111110110000011110000000001010010011110100001011001111010100110011000010100101010001100'
    
    operations_list = []
    
    operations = {0 : "sum", 1: "product", 2: "min", 3: "max", 4: "num",  5: ">", 6: "<", 7: "="}
    
    decode(packet, operations_list, operations)
    
    for operation in operations_list:
        print(operation)
    
    print('\n')
    
    print(evaluate_expr(operations_list))
    
    
    
    
    
    
    
    
        