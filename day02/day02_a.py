from aocd import lines

h_pos = 0
depth = 0

for line in lines :
    splitted_line = line.split(' ')
    cmd, amount = splitted_line[0], int(splitted_line[1])
    
    if cmd == 'forward':
        h_pos += amount
    elif cmd == 'down':
        depth += amount
    elif cmd == 'up':
        depth -= amount
    else :
        print('Warning : Unknown command {}, ignoring', cmd)

final_h_pos = depth * h_pos
print(final_h_pos)