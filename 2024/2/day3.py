from functools import reduce

strings = []

with open("day3.txt", "r") as file:
    for line in file:
        strings.append(line.strip())

def find_X_and_Y(s: str) -> tuple:
    # not valid
    if not s:
        return (0, 0)
    if ' ' in s:
        return (0, 0)
    if not ',' in s:
        return (0, 0)
    
    l = s.split(',')
    if len(l) != 2 :
        return (0, 0)
    
    if not (0 < len(l[0]) < 4 and  0 < len(l[1]) < 4):
        return (0, 0)
    
    try:
        x = int(l[0])
        y = int(l[1])
        return (x, y)
    except ValueError as e:
        return (0, 0)

def find_valid_mul(s: str, offset: int) -> list:
    if len(s) < 6:
        return []
    try:
        start_index = s.index('mul')
    except ValueError as e:
        return []
    left_parenthesis_index = start_index + 3
    if s[left_parenthesis_index] == '(':
        # search for right parenthesis after the first opening parenthesis
        try:
            right_parenthesis_index = (left_parenthesis_index + 1) + s[(left_parenthesis_index + 1):].index(')')
        except ValueError as e:
            return []

        between_parenthesis = s[(left_parenthesis_index + 1) : right_parenthesis_index]
        res = find_X_and_Y(between_parenthesis)
        if res != (0, 0):
            return [(offset + start_index, offset + right_parenthesis_index), res]
        else:
            return find_valid_mul(s[left_parenthesis_index + 2:], offset + left_parenthesis_index + 2)
    else:
        return find_valid_mul(s[left_parenthesis_index + 1:], offset + left_parenthesis_index + 1)

muls = []
for string in strings:
    i = 0
    while i < len(string):
        res = find_valid_mul(string[i:], i)
        if res == []:
            break
        i = res[0][1]
        muls.append(res[1])

print(muls)

ans = sum(a * b for (a, b) in muls)
print(ans)