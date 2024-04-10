#  check if sum of digits in 2 params is equal

# define a function
def is_equal(first_number, second_number):

    strfirst_number = str(first_number)
    strsecond_number = str(second_number)
    result1 = 0
    result2 = 0

    for digit in strfirst_number:
        result1 += int(digit)

    for digit in strsecond_number:
        result2 += int(digit)

    return result1 == result2

# call the function
first_number = input()
second_number = input()
result = is_equal(first_number, second_number)
print(result)


#break up digits by converting int to str.
#convert, and sum numbers in iteration variable result1
#repeat for second number in result2
#compare result1 and result 2
#return result