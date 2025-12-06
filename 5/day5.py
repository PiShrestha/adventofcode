from functools import reduce

r = True
ranges = []
ids = []
with open("day5.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            r = False
            continue
        if r:
            row = line.strip().split('-')
            ranges.append((int(row[0]), int(row[1])))
        else:
            ids.append(int(line.strip()))
        

count = 0
for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            count += 1
            break

sorted_ranges = sorted(ranges, key = lambda item: item[0])

new_ranges = []
run = False

left = sorted_ranges[0][0]
right = sorted_ranges[0][1]

for i in range(1, len(sorted_ranges)):
    curr_right = sorted_ranges[i - 1][1]
    right = max(right, curr_right)
    next_left = sorted_ranges[i][0]
    if right < next_left:
        new_ranges.append((left, right))
        left = next_left
    
    if i == len(sorted_ranges) - 1:
        new_ranges.append((left, sorted_ranges[i][1]))

diff = [x[1] - x[0] + 1 for x in new_ranges]
total = sum(diff)
print(total)