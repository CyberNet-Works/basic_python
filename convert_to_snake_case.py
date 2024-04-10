'''
thought process:
whenever you see a capital letter, switchcase and prepend "_"
'''

def convert_to_snake_case(s):
    result = ""
    for x in s:
        if x.islower():
            result += x
        else:
            result += x.replace(x,f"_{x.lower()}")
    return result

# take user input
input_string = input()

# display the result
print(convert_to_snake_case(input_string))


'''Challenge:
Convert camelCase to snake_case
Medium
Problem Description
Write a program to convert a string in camelCase to snake_case.

Define a function named convert_to_snake_case() that takes a single string in as an argument.
Inside the function, convert the string to snake_case and return it.
Example'''