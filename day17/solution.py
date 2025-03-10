def get_combo_operand_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    
    return registers[operand - 4]


def apply(operation, operand, registers, output):
    match operation:
        case 0:
            registers[0] = registers[0] // (2 ** get_combo_operand_value(operand, registers))
        
        case 1:
            registers[1] = registers[1] ^ operand
        
        case 2:
            registers[1] = get_combo_operand_value(operand, registers) % 8
            
        case 4:
            registers[1] = registers[1] ^ registers[2]
        
        case 5:
            output.append(get_combo_operand_value(operand, registers) % 8)
        
        case 6:
            registers[1] = registers[0] // (2 ** get_combo_operand_value(operand, registers))
        
        case 7:
            registers[2] = registers[0] // (2 ** get_combo_operand_value(operand, registers))
            
def binary_string_gen(zeroes, begining):
    return begining + '0' * zeroes
    
                
            



with open("input.txt", 'r') as file:
    lines = file.readlines()
    registers = []
    
    for line in lines[:3]:
        registers.append(int(line.strip('\n').split(":")[1][1::]))
    
    
    program = [2,4,1,1,7,5,1,5,4,0,0,3,5,5,3,0]
    
    
    
    print(binary_string_gen(0, '100101011010011000111001011011010110111010111101'))
    
    
    
    
    
    # for i in range(2**47, 2**48 + 1):
    #     print(i)
    index = 0
    output = []

    while index < len(program):
        operation = program[index]
        operand = program[index + 1]
        
        if operation == 3 and not registers[0] == 0:
            index = operand
            continue
        
        apply(operation, operand, registers, output)
        
        index = index + 2
    
    print(output)

    # if output == program:
    #     print('Hurray')
    #     print(i)
        # break

    
    