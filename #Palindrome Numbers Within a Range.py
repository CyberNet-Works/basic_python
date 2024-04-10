#Palindrome Numbers Within a Range

def count_palindromes(start_number, end_number):
    therange = list(range(start_number, end_number + 1))
    count = 0
    temp = ""

    for num in therange:
        if str(num) == str(num)[::-1]:
            count += 1
    return count
        
        

# take the integer input 
start_number = int(input())
end_number = int(input())
# call the function
print(count_palindromes(start_number, end_number))

'''
Challenge:
Palindrome Numbers Within a Range
Easy
Problem Description
Write a Python program to count the number of palindrome numbers within a given range.

A palindrome number is a number that remains the same when its digits are reversed.

For example, numbers like 121, 1, 22 are palindrome numbers because their digits remain the same when reversed.

Define a function named count_palindromes() with two arguments: start_number and end_number.
Inside the function, return the total count of palindrome numbers.
Example
Test Input

10
20
Expected Output

1
Note: Both start_number and end_number in the range are inclusive.


'''