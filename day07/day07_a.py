from aocd import lines
import statistics

positions = list(map(int, lines[0].split(',')))
# Get the median to know which distances we have to calculate
median = round(statistics.median(positions))
distances = sum(abs(median - pos) for pos in positions)

print(distances)
