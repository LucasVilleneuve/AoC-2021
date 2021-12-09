from aocd import lines

total = 0
for line in lines:
    splitted_line = line.split('|')
    inputs = splitted_line[1].split(' ')
    
    total += sum([1 for nb in inputs if len(nb) == 2 or len(nb) == 3 or len(nb) == 4 or len(nb) == 7])

print(total)