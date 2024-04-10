#check for sequential chars in string:

def same_subsequent(string):
    stringlength = len(string)

    for i in range(stringlength - 1):
        if string[i] == string[i + 1]:
            return string[i]
    
letter = same_subsequent('hello')
print(letter)