def smallest_multiple(digits, multiple_of):
    highest = []
    for x in range(1, 10 ** (digits - 1)):
        if x * multiple_of < (10 ** (digits - 1)):
            pass
        else:
            highest.append(x * multiple_of)

    return highest[0]


# take user input
digits = int(input())
multiple_of = int(input())

# call the function
print(smallest_multiple(digits, multiple_of))