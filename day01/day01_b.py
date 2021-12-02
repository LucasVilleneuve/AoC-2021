from aocd import numbers

if len(numbers) < 4 :
    print("Error, not enough measurements to take a guess.")
    exit(0)
    
old_sliding_window = sum(numbers[:3])
increases = 0

for i in range(3, len(numbers)) :

    sliding_window = sum(numbers[i-2:i+1])
    if sliding_window > old_sliding_window :
        increases = increases + 1

    old_sliding_window = sliding_window

print(increases)