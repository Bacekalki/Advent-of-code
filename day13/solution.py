from fractions import Fraction
import numpy as np

def invert_matrix(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError as e:
        print("Error:", e)
        return None

def get_indeces(line1, line2):
    
    splitted1 = line1.split("+")
    splitted2 = line2.split("+")
    
    # print(splitted1)
    # print(splitted2)
    
    
    list1 = []
    list2 = [int(splitted1[-1]), int(splitted2[-1])]
    
    new_split1 = splitted1[1].split(",")
    new_split2 = splitted2[1].split(",")
    
    list1.insert(0, int(new_split2[0]))
    list1.insert(0, int(new_split1[0]))
   
    
    return [list1, list2]

def get_target(line):
    splitted = line.split("=")
    my_list = [int(splitted[-1])]
    
    new_split = splitted[1].split(",")
    my_list.insert(0, int(new_split[0]))
    
    return my_list
    
def solve_system(A, b):
    for i in range(101):
        for j in range(101):
            if i * A[0][0] + j * A[0][1] == b[0] and i * A[1][0] + j * A[1][1] == b[1]:
                return (i, j)
    
    return (0, 0)
            
            
        

with open("input.txt", 'r') as file:
    lines = file.readlines()
    solutions = []
    
    my_sum = 0
    
    for i in range(0, len(lines), 4):
        A = get_indeces(lines[i].strip('\n'), lines[i + 1].strip('\n'))
        b = get_target(lines[i + 2].strip('\n'))
        
        if solve_system(A, b) == (0, 0):
            sol = np.dot(invert_matrix(A), np.array([10000000000000 + b[0], 10000000000000 + b[1]]))
            my_sum += 3 * sol[0] + sol[1]
            
        
        
    
    print(my_sum)
        
        
    
    # my_sum = 0
    
    # for solution in solutions:
    #     my_sum += 3 * (solution[0]) + solution[1]

    # print(my_sum)
            
        