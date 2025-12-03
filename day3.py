nums = []
with open("day3.txt", "r") as file:
    for line in file:
        nums.append(int(line.strip()))
        
def find_max_2digit(num: int) -> int:
    num_str = str(num)
    largest_first_digit = int(max(list(num_str[:-1])))
    largest_first_digit_index = list(num_str[:-1]).index(str(largest_first_digit))
    largest_second_digit = int(max(list(num_str[largest_first_digit_index + 1:])))
    largest_first_digit_index = list(num_str[largest_first_digit_index + 1:]).index(str(largest_second_digit))
    return largest_first_digit * 10 + largest_second_digit

def find_max_kdigit(num: int, k: int) -> int:
    num_str = str(num)
    right_index = len(num_str) - k + 1

    left_index = 0
    ans = 0

    for i in range(k):
        sub_array = list(num_str[left_index:right_index])
        digit = int(max(sub_array))
        left_index = left_index + sub_array.index(str(digit)) + 1
        right_index += 1
        ans = ans * 10 + digit

    return ans

total = 0
for num in nums:
    total += find_max_kdigit(num, 12)

print(total)