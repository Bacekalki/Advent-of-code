from collections import defaultdict
import heapq

def generate_new_map(first_map):
    
    new_map = [[0 for _ in range(len(first_map[0]) * 5)] for _ in range(len(first_map) * 5)]
    
    for i in range(len(new_map)):
        for j in range(len(new_map[0])):
            toAdd = i // len(first_map) + j // len(first_map[0])
            new_val = first_map[i % len(first_map)][j % len(first_map[0])] + toAdd
            if new_val > 9:
                new_val = new_val - 9
            
            new_map[i][j] = new_val

    
    return new_map
    
    
    
    
    
class Pair:
    dp = defaultdict(lambda: 99_999_999)
    
    def __init__(self, x, y, value = 0):
        self.x = x
        self.y = y
        self.value = value
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __lt__(self, other):
        to_Add_self = min(Pair.dp[Pair(self.x - 1, self.y)], Pair.dp[Pair(self.x + 1, self.y)], Pair.dp[Pair(self.x, self.y - 1)], Pair.dp[Pair(self.x, self.y + 1)])
        if to_Add_self == 99_999_999:
            to_Add_self = 0
        
        val_1 = self.value + to_Add_self
        
        to_Add_other = min(Pair.dp[Pair(other.x - 1, other.y)], Pair.dp[Pair(other.x + 1, other.y)], Pair.dp[Pair(other.x, other.y - 1)], Pair.dp[Pair(other.x, other.y + 1)])
        if to_Add_other == 99_999_999:
            to_Add_other = 0
        
        val_2 = other.value + to_Add_other
        
        return val_1 < val_2
        
    

with open("input.txt", 'r') as file:
    lines = file.readlines()
    map = [[int(char) for char in line if not char == '\n'] for line in lines]
    map = generate_new_map(map)
    
    print(map)
    my_dict = defaultdict(lambda: 99_999_999)
    for i in range(len(map)):
        for j in range(len(map[0])):
            my_dict[Pair(i, j)] = map[i][j]
    
    counter = 0
    
    q = []
    heapq.heappush(q, Pair(0, 0, my_dict[Pair(0, 0)]))
    
    already_visited = set()
    
    while len(q) > 0:
        current = heapq.heappop(q)
        already_visited.add(current)
        
        to_Add = min(Pair.dp[Pair(current.x - 1, current.y)], Pair.dp[Pair(current.x + 1, current.y)], Pair.dp[Pair(current.x, current.y - 1)], Pair.dp[Pair(current.x, current.y + 1)])
        if to_Add == 99_999_999:
            to_Add = 0
        
        Pair.dp[current] = my_dict[current] + to_Add
        
        pot_neighbours = [Pair(current.x - 1, current.y, my_dict[Pair(current.x - 1, current.y)]), Pair(current.x + 1, current.y, my_dict[Pair(current.x + 1, current.y)]), Pair(current.x, current.y - 1, my_dict[Pair(current.x , current.y - 1)]), Pair(current.x, current.y + 1, my_dict[Pair(current.x, current.y + 1)])]
        
        for neighbour in pot_neighbours:
            if 0 <= neighbour.x <= len(map) - 1 and 0 <= neighbour.y <= len(map[0]) - 1 and neighbour not in already_visited:
                already_visited.add(neighbour)
                heapq.heappush(q, neighbour)
        
        
    print(Pair.dp[Pair(len(map) - 1, len(map[0]) - 1)])