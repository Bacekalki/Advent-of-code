from collections import defaultdict

with open("input.txt", 'r') as file:
    input = file.readline()
    stones = [int(stone) for stone in input.strip('\n').split(" ")]
    
    dict = defaultdict(lambda: 0, {stone: 1 for stone in stones})
    
    print(dict)
    
    for step in range(75):
        new_dict = dict.copy()
        for key, value in dict.items():
            if dict[key] <= 0:
                continue
            
            if key == 0:
                new_dict[key] = new_dict[key] - value
                new_dict[1] = new_dict[1] + value
                continue
            
            if len(str(key)) % 2 == 0:
                str_key = str(key)
                left = str_key[:len(str_key)//2]
                right = str_key[len(str_key)//2:]
                new_dict[int(left)] += value
                new_dict[int(right)] += value
                new_dict[key] -= value
                continue
            
            new_dict[key] -= value
            new_dict[key * 2024] += value
        
        dict = defaultdict(lambda: 0, filter(lambda pair: pair[1] > 0, new_dict.items()))
        

print(sum(value for value in dict.values()))
    
    

            