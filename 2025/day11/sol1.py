from queue import Queue
def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        graph : dict[str, list[str]] = {}
        for line in lines:
            line = line.strip().split(' ')
            key = line[0][:-1]
            graph[key] = line[1:]
        
        return graph

def solve(graph : dict[str, list[str]]):
    start = 'you'
    end = 'out'
    q : Queue[str] = Queue()
    q.put(start)
    c = 0
    while not q.empty():
        current = q.get()
        
        if current == end:
            c += 1
            continue
        
        children = graph[current]
        for child in children:
            q.put(child)
    
    return c

if __name__ == "__main__":
    print(solve(read_input()))
    
    
    