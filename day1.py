rotations = []

with open("day1.txt", "r") as file:
    for line in file:
        rotations.append(line.strip())

count = 0
max = 100
curr = 50
for rotation in rotations:
    if curr == 0:
        count += 1
    num_rotations = int(rotation[1:])
    count += num_rotations // max
    num_rotations = num_rotations % max
    orig_curr = curr
    
    if rotation.startswith('R'):
        curr = (curr + num_rotations)
        if orig_curr != 0 and curr > 100:
            print("R", num_rotations, curr)
            count += 1
        curr = curr % max
    # Left
    else:
        curr = (curr - num_rotations)
        if orig_curr != 0 and curr < 0:
            print("L", num_rotations, curr)
            count += 1
        curr = curr % max

if curr == 0:
    count += 1

print(count)
