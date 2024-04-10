#Using Recursion to Check if String Is Palindrome
def is_string_palindrome(string):
    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False

    return is_string_palindrome(string[1:-1])

# take user input
user_input = input()

# call the function
print(is_string_palindrome(user_input.lower()))

'''
Using Recursion to Check if String Is Palindrome
Medium
Problem Description
Write a program to recursively determine if a string is a palindrome.

A palindrome is a word, phrase, number, or other sequences of characters that reads the same backward or forward. For this challenge, an empty string counts as a palindrome.

Recursion is a programming concept that involves a function calling itself within its own definition.

Define a function named is_string_palindrome() with a single argument string.
Inside the function, implement recursion to return True if the string is a palindrome, else return False.

'''