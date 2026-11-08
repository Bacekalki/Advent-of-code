from functools import cache

@cache
def can_towel_be_made(towel, designs):
    count = 0
    if towel == '':
        count += 1
    
    for design in designs:
        length = len(design)
        if design == towel[:length]:
            count = count + can_towel_be_made(towel[length:], designs)
    
    return count


    



with open("input.txt", 'r') as file:
    lines = file.readlines()
    designs = lines[0].strip('\n').split(', ')
    my_set = frozenset(designs)
    towels_to_make = [line.strip('\n') for line in lines[2::]]
    
    count = 0
    i = 0
    
    for towel in towels_to_make:
        #print(i)
        count += can_towel_be_made(towel, my_set)
        
        #i+=1
    
    print(count)
        
    
            
    
    