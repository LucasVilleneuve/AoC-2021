from aocd import numbers

old_depth = numbers[0]
increases = 0

for depth in numbers[1:] :
    if depth > old_depth :
        increases = increases + 1
        
    old_depth = depth
    
print(increases)