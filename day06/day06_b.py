from aocd import lines

nb_days = 256
# Create a list with the number of fish for each days left before reproducing
timers = [0] * 9

# Add our initial fish
for fish in lines[0].split(','):
    timers[int(fish)] += 1

for day in range(1, nb_days + 1):
    # Number of fish who reproduced
    new_fish = timers[0]

    # Decrement days left for each fish
    for i in range(8):
        timers[i] = timers[i + 1]

    # Fish who reproduced are back on the 6 day timer
    timers[6] += new_fish

    # Add the new fish (8 day timer)
    timers[8] = new_fish

nb_fish = sum(timers)
print(nb_fish)