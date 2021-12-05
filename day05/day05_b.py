from aocd import lines


def is_line_diagonal(pos1, pos2):
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


vent_lines = []

for line in lines:
    # Convert string to a list of 2 positions
    positions = [list(map(int, pos.split(','))) for pos in line.split(' -> ')]
    
    # Only add horizontal and vertical lines and diagonal lines
    if positions[0][0] == positions[1][0] or \
    positions[0][1] == positions[1][1] or \
    is_line_diagonal(positions[0], positions[1]):
        vent_lines.append(positions)
 
 
# Get the biggest position to get the floor's size
size = max(nb for line in vent_lines for pos in line for nb in pos) + 1

# Create a 2D array representing the floor
floor = [['0'] * size for i in range(size)]

# Add vent lines to the floor
for line in vent_lines:
    start = line[0]
    end = line[1]
    
    cur_x = start[0]
    cur_y = start[1]
    
    while cur_x != end[0] or cur_y != end[1]:
        floor[cur_y][cur_x] = str(int(floor[cur_y][cur_x]) + 1)
        
        if cur_x < end[0]:
            cur_x += 1
        elif cur_x > end[0]:
            cur_x -= 1

        if cur_y < end[1]:
            cur_y += 1
        elif cur_y > end[1]:
            cur_y -= 1
    floor[cur_y][cur_x] = str(int(floor[cur_y][cur_x]) + 1)

# Find +2 times overlap points
nb_overlap_points = sum(1 for row in floor for cell in row if int(cell) >= 2)
print(nb_overlap_points)
