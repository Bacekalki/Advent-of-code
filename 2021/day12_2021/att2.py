from collections import defaultdict, deque

with open("input2.txt", 'r') as file:
    lines = file.readlines()
    adjecency_list = defaultdict(list)
    for line in lines:
        splitted = line.split("-")
        adjecency_list[splitted[0]].append(splitted[1].strip())
        adjecency_list[splitted[1].strip()].append(splitted[0])


def bfs_paths(start, end):
    queue = deque([(start, [start])])
    all_paths = []

    while queue:
        node, path = queue.popleft()
        for neighbor in adjecency_list[node]:
            if neighbor.islower() and neighbor in path:
                continue
            new_path = path + [neighbor]
            if neighbor == end:
                all_paths.append(new_path)
            else:
                queue.append((neighbor, new_path))
    return all_paths

paths = bfs_paths("start", "end")
for p in paths:
    print(p)
print("Total paths:", len(paths))

    