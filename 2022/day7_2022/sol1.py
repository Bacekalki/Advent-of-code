class File:
    def __init__(self, line : str):
        size, name = line.split(' ')
        size = int(size)
        self.size = size
        self.name = name

    def __str__(self) -> str:
        return f"File : {self.name} with size : {self.size}"
        
class Directory:
    def __init__(self, parent, name : str):
        self.content : list[Directory | File] = []
        self.parent : Directory | None = parent
        self.name = name
        
    def calculate_size(self) -> int:
        size = 0
        for item in self.content:
            if isinstance(item, Directory):
                size += item.calculate_size()
            else:
                size += item.size
        
        return size
    
    def __str__(self) -> str:
        output = ""
        output += f"Directory : {self.name} with items : "
        for item in self.content:
            output += str(item)
        
        return output

def get_directories(root : Directory | File, directories : list[Directory]) -> list[Directory]:
    if isinstance(root, Directory):
        directories.append(root)
        for item in root.content:
            get_directories(item, directories)

def parseInput():
    current_directory : Directory | None = Directory(None, "")
    
    with open('input.txt', 'r') as input:
        lines = input.readlines()
        for index, line in enumerate(lines):
            # print(current_directory.name)
            line = line.strip()
            if line[:4] == "$ cd":
                splitted = line.split(' ')
                if splitted[2] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = Directory(current_directory, splitted[2])
            
            if "$ ls" in line:
                for i in range(index + 1, len(lines)):
                    if lines[i][0] == "$":
                        break
                    if lines[i][:3] == "dir":
                        name = lines[i].split(' ')[1].strip()
                        current_directory.content.append(Directory(current_directory, name))
                    else:
                        current_directory.content.append(File(lines[i].strip()))
                
                parent = current_directory.parent
                if parent is not None:
                    for index, item in enumerate(parent.content):
                        if item.name == current_directory.name:
                            parent.content[index] = current_directory
                        
        
        while not current_directory.name == '/':
            current_directory = current_directory.parent
        
        return current_directory


        
if __name__ == "__main__":
    root = parseInput()
    directories : list[Directory] = []
    get_directories(root, directories)
    free_space = 70000000 - root.calculate_size()
    desired_space = 30000000
    
    best_diff = 70000000
    best_dir = root
    
    for dir in directories:
        new_space = free_space + dir.calculate_size()
        if new_space >= desired_space:
            diff = new_space - desired_space
            if diff < best_diff:
                best_diff = diff
                best_dir = dir
    
    print(best_dir.calculate_size())
        


            
                        
            
            
                