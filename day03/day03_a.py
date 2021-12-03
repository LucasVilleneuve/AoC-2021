from aocd import lines

if len(lines) < 1 :
    print("Error, not enough diagnostic reports to evaluate power consumption.")
    exit(0)

gamma = 0

# Iterate to get gammma
for i in range(0, len(lines[0])):
    occurences = sum(1 for x in lines if x[i] == "1")
    if occurences > (len(lines) / 2):
        gamma = (gamma << 1) + 1
    else :
        gamma = gamma << 1

mask = (1 << len(lines[0])) - 1 # Calculate mask to invert gamma
epsilon = gamma ^ mask
power_cons = gamma * epsilon

print('Power consumuption is {}'.format(power_cons))