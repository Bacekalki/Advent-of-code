from collections import defaultdict
from queue import Queue

class Node:
    def __init__(self, name, previous_nodes = [], can_visit_twice = True):
        self.name = name
        self.previous_nodes = previous_nodes
        self.can_visit_twice = can_visit_twice
        
        
def countPaths(adjecency_list):
    end_counter = 0
    q = Queue()
    q.put(Node('start'))
    
    while not q.empty():
        current = q.get()
        
        if current.name == 'end':
            end_counter = end_counter + 1
            current.previous_nodes.append('end')
            print(current.previous_nodes)
            continue
        
        available = []
        for elem in adjecency_list[current.name]:
            if elem.isupper():
                available.append(Node(elem, current.previous_nodes.copy(), current.can_visit_twice))
            
            else:
                if not elem == 'start':
                    
                    if elem not in current.previous_nodes:
                        available.append(Node(elem, current.previous_nodes.copy(), current.can_visit_twice))
                    else:
                        if current.can_visit_twice:
                            available.append(Node(elem, current.previous_nodes.copy(), False))
            
            
        for node in available:
            node.previous_nodes.append(current.name)
        
        for node in available:
            q.put(node)

    return end_counter 


with open("input.txt", 'r') as file:
    lines = file.readlines()
    adjecency_list = defaultdict(list)
    for line in lines:
        splitted = line.split("-")
        adjecency_list[splitted[0]].append(splitted[1].strip())
        adjecency_list[splitted[1].strip()].append(splitted[0])
        
    print(countPaths(adjecency_list))
    