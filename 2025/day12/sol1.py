def read_input():
    with open('input.txt', 'r') as file:
        shapes = [9, 9, 9, 9, 9]
        areas : list[int] = []
        requirements : list[list[int]] = []
        lines = file.readlines()
        lines = lines[30:]
        
        for line in lines:
            line = line.strip().split(' ')
            x, y = line[0][:-1].split('x')
            areas.append(int(x) * int(y))
            requirements.append(list(map(int, line[1:])))
        
        return shapes, areas, requirements


def find_unsolvable(shapes : list[int], areas : list[int], requirements : list[list[int]]):
    unsolvable : set[int] = set()
    i = 0
    for area, reqs in zip(areas, requirements):
        total = 0
        for num, shape in zip(reqs, shapes):
               total += (num * shape)
        i = i + 1
        if total > area:
            unsolvable.add(i)
    
    return unsolvable

if __name__ == "__main__":
    shapes, areas, requirements = read_input()
    print(1000 - len(find_unsolvable(shapes, areas, requirements)))