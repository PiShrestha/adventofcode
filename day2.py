from functools import reduce
ids = []

with open("day2.txt", "r") as file:
    for line in file:
        ids = line.split(",")

id_ranges = []
for id_range in ids:
    id_str = id_range.split("-")
    id_ranges.append((int(id_str[0]), int(id_str[1])))

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def is_invalid(num: int) -> bool:
    num_in_str = str(num)
    length = len(num_in_str)
    factors = find_factors(length)

    factors.remove(length)

    for factor in factors:
        i = factor
        j = factor + factor
        while j <= length:
            if num_in_str[i - factor: i] != num_in_str[i: j]:
                break
            i = j
            j += factor

        if i == length:
            return True
    
    return False
        

invalid_ids = []
for id_range in id_ranges:
    for num in range(id_range[0], id_range[1] + 1):
        if is_invalid(num):
            invalid_ids.append(num)

total = reduce(lambda x, y: x + y, invalid_ids)

print(total)