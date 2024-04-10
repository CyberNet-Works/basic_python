#Check Palindrome Dates
def is_date_palindromic(date_in_string):
    date_in_string = date_in_string.replace("/","")

#    return date_in_string[0:2], date_in_string[2:4]

    if date_in_string[0:2] == date_in_string[2:4] and date_in_string == date_in_string[::-1]:
        return True
    else:
        return False
    
    

# take user input
date_in_string = input()

# call the function
print(is_date_palindromic(date_in_string))


'''Check Palindromic Dates
Medium
Problem Description
Write a program to check if a given date is a palindromic date in both dd/mm/yyyy and mm/dd/yyyy formats.

Define a function named is_date_palindromic() that accepts a single argument date_in_string (a date string in the dd/mm/yyyy format).
The function should return True if the given date is palindromic in both the dd/mm/yyyy and mm/dd/yyyy formats. Otherwise, it should return False.
'''