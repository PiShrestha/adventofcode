nums = []
rows = []

with open("day6.txt", "r") as file:
    for line in file:
        row = line
        rows.append(row[:-1])
        row = row.strip().split()
        if row[0] in "+*":
            ops = row
        else:
            num = [int(s) for s in row]
            nums.append(num)

rows = rows[:-1]

nums = []
column = []

for i in range(len(rows[0]) - 1, -1, -1):
    all_empty = True
    num = ''
    for j in range(len(rows)):
        num = num + rows[j][i] if rows[j][i] != ' ' else num + ''
        if num != '':
            all_empty = False
        
    # new column started, reset the num variable
    if all_empty:
        nums.insert(0, column)
        column = []
    else:
        column.append(int(num))
        num = ''

nums.insert(0, column)          

print(nums)

total = 0

# # part 1
# for i in range(len(nums[0])):
#     if ops[i] == '+':
#         for j in range(len(nums)):
#             total += nums[j][i]
#     else:
#         prod = 1
#         for j in range(len(nums)):
#             prod *= nums[j][i]
        
#         total += prod

# part 2
for i in range(len(nums)):
    if ops[i] == '+':
        for j in range(len(nums[i])):
            total += nums[i][j]
    else:
        prod = 1
        for j in range(len(nums[i])):
            prod *= nums[i][j]
        
        total += prod

print(total)