import ast
from queue import Queue
def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        end_states : list[tuple[int, ...]] = []
        buttons : list[list[tuple[int, ...] | int]] = []
        joltage_reqs : list[list[int]] = []
        for line in lines:
            line = line.strip().split()
            end_state = tuple(map(lambda x: 0 if x == '.' else 1, list(line[0][1:-1])))
            end_states.append(end_state)
            joltage = line[-1][1:-1].split(',')
            joltage = list(map(int, joltage))
            joltage_reqs.append(joltage)
            current : list[tuple[int, ...] | int] = []
            for button in line[1:-1]:
                button = ast.literal_eval(button)
                current.append(button)
            buttons.append(current)
    
    return end_states, buttons, joltage_reqs

def push_button(current_state : tuple[int, ...], button : tuple[int, ...] | int):
    if isinstance(button, int):
        button = (button, )
    
    new_state = list(current_state)
    for index in button:
        new_state[index] = new_state[index] ^ 1
    
    return tuple(new_state)
        
def get_children(current_state : tuple[int, ...], buttons : list[tuple[int, ...] | int]):
    children : list[tuple[int, ...]] = []
    for button in buttons:
        children.append(push_button(current_state, button))
    
    return children

def bfs(end : tuple[int, ...], buttons : list[tuple[int, ...] | int]) -> int:
    n = len(end)
    start = tuple(0 for _ in range(n))
    q : Queue[tuple[tuple[int, ...], int]] = Queue()
    q.put((start, 0))
    visited : set[tuple[int, ...]] = set()
    
    while not q.empty():
        current_state, moves_so_far = q.get()
        
        if current_state == end:
            return moves_so_far
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        children = get_children(current_state, buttons)
        for child in children:
            if child in visited:
                continue
            q.put((child, moves_so_far + 1))

def solve(end_states : list[tuple[int, ...]], buttons : list[list[tuple[int, ...] | int]]):
    total = 0
    for end_state, buttons_list in zip(end_states, buttons):
        total += bfs(end_state, buttons_list)
    
    return total
        
    

if __name__ == "__main__":
    end_states, buttons, _ = read_input()
    print(solve(end_states, buttons))