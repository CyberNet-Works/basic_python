def find_highest_number(numbers_list):
    if len(numbers_list) == 0:
        return -float('inf')
    elif len(numbers_list) == 1:
        return numbers_list[0]

    for i in range(0, len(numbers_list) - 1):
        if numbers_list[i] > numbers_list[i + 1]:
            numbers_list[i + 1] = numbers_list[i]

    return find_highest_number(numbers_list[1:])

# take user input
numbers_list = list(map(int, input().split()))

# print the highest number
print(find_highest_number(numbers_list))


