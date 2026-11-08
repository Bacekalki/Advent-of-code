from queue import Queue
with open("input.txt", 'r') as file:
    line = file.readline()
    current_id = 0
    translated = []
    index = 0
    files_list = []
    empty_spaces = []
    

    for i in range(len(line)):
        start = 0
        end = 0
        for j in range(int(line[i])):
            if j == 0:
                start = index
            if i % 2 == 0:
                translated.append(current_id)
            else:
                translated.append('.')
            
            index = index + 1
        
        end = index - 1
        
        if i % 2 == 0:
            files_list.insert(0, (current_id, start, end))
            current_id += 1
        else:
            if not (int(line[i])) == 0:
                empty_spaces.append((start, end))
                
                
        

moved_files = 0
index_i = 0
change_in_files = []

for file in files_list:
    index_i += 1
    index_j = 0
    for empty_space in empty_spaces:
        index_j = index_j + 1
        
        if file[1] < empty_space[0] and file[2] < empty_space[1]:
            continue
        
        if empty_space[1] - empty_space[0] >= file[2] - file[1]:
            filled_spaces = 0
            moved_files += 1
            # print("Moved file")
            # print(file)
            for i in range(empty_space[0], empty_space[1] + 1):
                translated[i] = file[0]
                translated[file[1] + filled_spaces] = '.'
                filled_spaces += 1
                if filled_spaces == file[2] - file[1] + 1:
                    break
            
            empty_spaces.append((file[1], file[2]))
            files_list[index_i - 1] = (file[0], empty_space[0], empty_space[0] + filled_spaces - 1)
            #change_in_files.append((file[0], empty_space[0], empty_space[0] + filled_spaces - 1))
            empty_spaces[index_j - 1] = (empty_space[0] + filled_spaces, empty_space[1])
            break
    



sum = 0

for index, value in enumerate(translated):
    if not value == '.':
        sum += index * value


print(sum)
        

    