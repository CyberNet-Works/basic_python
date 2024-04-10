def digits_counter(string):

    result = 0

    for char in string:
        if char.isnumeric():
            result += 1

    return result



string = input()
result = digits_counter(string)
print(result)