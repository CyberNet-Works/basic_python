def is_lapindrome(number):
    str_num = str(number)
    num_length = len(str_num)
    split = num_length // 2

    # Extract the first and second halves
    first_half = sorted(str_num[:split])
    if num_length % 2 == 0:
        second_half = sorted(str_num[split:])
    else:
        second_half = sorted(str_num[split + 1:])

    # Check if the sorted halves are equal
    if first_half == second_half:
        return "It is Lapindrome Number"
    else:
        return "It is not Lapindrome Number"

number = input("Enter a number: ")
result = is_lapindrome(number)
print(result)
