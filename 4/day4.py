rolls = []

with open("day4.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        rolls.append(row)

def get_roll_paper_indices(rolls: list) -> list:
    ans = []
    for i, row in enumerate(rolls):
        for j, roll in enumerate(row):
            adjacent_count = 0

            # top left
            if i != 0 and j != 0 and rolls[i-1][j-1] == '@':
                adjacent_count += 1
            # mid left
            if j != 0 and j != 0 and rolls[i][j-1] == '@':
                adjacent_count += 1
            # bottom left
            if i != len(rolls) - 1 and j != 0 and rolls[i+1][j-1] == '@':
                adjacent_count += 1

            # mid top
            if i != 0 and rolls[i-1][j] == '@':
                adjacent_count += 1
            # mid bottom
            if i != len(rolls) - 1 and rolls[i+1][j] == '@':
                adjacent_count += 1

            # top right
            if i != 0 and j != len(rolls[0]) - 1 and rolls[i-1][j+1] == '@':
                adjacent_count += 1
            # mid right
            if j != len(rolls[0]) - 1 and rolls[i][j+1] == '@':
                adjacent_count += 1
            # bottom right
            if i != len(rolls) - 1 and j != len(rolls[0]) - 1 and rolls[i+1][j+1] == '@':
                adjacent_count += 1

            if roll == '@' and adjacent_count < 4:
                ans.append((i,j))

    return ans

indices_to_remove = get_roll_paper_indices(rolls)
count = len(indices_to_remove)
grand_count = count

while count > 0:
    for index in indices_to_remove:
        rolls[index[0]][index[1]] = '.'

    indices_to_remove = get_roll_paper_indices(rolls)
    count = len(indices_to_remove)
    grand_count += count

print(grand_count)


