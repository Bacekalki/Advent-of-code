from collections import defaultdict
from itertools import combinations
import networkx as nx

def is_clique(nodes, adj_dict):
    combs = list(combinations(nodes, 2))
    for x, y in combs:
        if y not in adj_dict[x]:
            return False
    
    return True
    


with open("input.txt", 'r') as file:
    lines = file.readlines()
    adj_dict = defaultdict(lambda: set())
    G = nx.Graph()
    for line in lines:
        splitted = line.strip('\n').split('-')
        # adj_dict[splitted[0]].add(splitted[1])
        # adj_dict[splitted[1]].add(splitted[0])
        G.add_edge(splitted[0], splitted[1])
    
    max_clique = nx.find_cliques(G)
    largest_clique = max(max_clique, key=len)

    print(','.join(sorted(largest_clique)))
    
    
    
    
    
    
    
    
    
    
    
            
    
        
    