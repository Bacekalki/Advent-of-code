class Page:
    
    comparator_set = set()
    
    def __init__(self, number):
        self.number = number
    
    def __lt__(self, other):
        return (self.number + "|" + other.number) in Page.comparator_set
    
    def __repr__(self) -> str:
        return self.number

with open("input.txt", 'r') as file:
    lines = file.readlines()
    switch_input = False
    list_of_reports = []
    
    for line in lines:
        if line == '\n':
            switch_input = True
            continue
            
        
        if not switch_input:
            Page.comparator_set.add(line.strip('\n'))
        else:
            list_of_reports.append([Page(num) for num in line.strip('\n').split(",")])
    
    
    copy_list = list_of_reports.copy()
    sorted_list = [sorted(elem) for elem in copy_list]
    sum = 0
    
    for i in range(len(sorted_list)):
        if not sorted_list[i] == list_of_reports[i]:
            sum = sum + int(sorted_list[i][len(sorted_list[i]) // 2].number)
    
    
    print(sum)
        
    
    
        
    
    
