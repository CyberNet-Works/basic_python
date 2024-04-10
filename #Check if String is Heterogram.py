#Check if String is Heterogram
def is_heterogram(s):
    s = s.lower().replace(" ", "")

    status = "Yes"

    for char in s:
        if s.count(char) > 1:
            status = "No"
    return status

# take user input
input_string = input()

# call the function
print(is_heterogram(input_string))

'''Check if String is Heterogram
Medium
Problem Description
Write a program to determine if a given string is a Heterogram or not.

A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than once.

Define a function named is_heterogram() with a single argument (string).
Inside the function, if the string is a heterogram, then return Yes, otherwise return No.
Note: Make the function case sensitive for now.

Example
Test Input

the big dwarf only jumps
Expected Output

Yes

'''