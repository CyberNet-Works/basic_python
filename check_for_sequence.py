def is_sequence(number_list):
    number_list = list(map(int, number_list))
    n = len(number_list)
    for i in range(n):
        if number_list[i] != i + 1:
            return False
    return True

# Get the input numbers as a list
number_list = input().split()

# Check if it's a sequence and print the result
result = is_sequence(number_list)
print(result)



