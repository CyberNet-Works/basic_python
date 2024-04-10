#count dupe characters, no special chars...

# define a function
def duplicate_counter(string):
    string = string.lower()
    dict = {}
    count = 0
    result = 0

    for char in string:
        if not char.isalpha():
            continue        
        elif char in dict:
            dict[char] += 1

        else:
            dict[char] = 1

    for first_dupe in dict:
        if dict[first_dupe] > 1:
            result += 1

    return result

# call the function
string = input()
result = duplicate_counter(string)
print(result)

#format string
#make dictionary to store key:count and value:char.  
#iterate to create dict
#iterate for result count of keys > 1
#return sum of count