from collections import defaultdict, Counter
from copy import deepcopy

with open("input.txt", 'r') as file:
    lines = file.readlines()
    start = lines[0].strip('\n')
    first_letter = start[0]
    last_letter = start[-1]
    rules = defaultdict(lambda: '')
    my_counter = defaultdict(lambda: 0)
    legit_counter = defaultdict(lambda: 0)
    for i in range(len(lines)):
        if i >= 2:
            splitted = lines[i].split("->")
            rules[splitted[0].strip()] = splitted[1][1::].strip('\n')
    
    for i in range(len(start) - 1):
        my_counter[start[i] + start[i + 1]] += 1
    
    copy = {}
    for step in range(40):
        copy = deepcopy(my_counter)
        for key, value in my_counter.items():
            if value > 0:
                copy[key[0] + rules[key]] += value
                copy[rules[key] + key[1]] += value
                copy[key] -= value
            
        
        for key, value in copy.items():
            my_counter[key] = value
    

    
    
    
    for key, value in my_counter.items():
        legit_counter[key[0]] += value
        legit_counter[key[1]] += value
    
    for key in legit_counter:
        legit_counter[key] = legit_counter[key] // 2
        
        if key == first_letter or key == last_letter:
            legit_counter[key] += 1
    
    
    vals = sorted(legit_counter.values())
    
    print(vals[-1] - vals[0])
        
    
        
     
        
    
    
        

    
    
    
            