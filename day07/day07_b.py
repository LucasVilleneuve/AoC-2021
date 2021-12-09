from aocd import lines

positions = list(map(int, lines[0].split(',')))

# Get the mean to know which distances we have to calculate
mean = round(int(sum(positions) / len(positions)))

total = 0
for pos in positions:
    distance = abs(mean - pos)
    triangular_number = distance * (distance + 1) / 2
    total += triangular_number

print(round(total))
