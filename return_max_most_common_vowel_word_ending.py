def count_common_vowel(string):
    string = string.lower()

    vowels = "aeiou"
    result = ""
    elements = string.split()
    data = {} #last letter, count

    for word in elements:
        if word[-1] in vowels:
            last_letter = word[-1]

            if last_letter in data:
                data[last_letter] += 1
            else: 
                data[last_letter] = 1  
        else:
            continue

    result = max(data, key=data.get)

    return result


# call the function
string = input()
result = count_common_vowel(string)
print(result)


#input str
#format lower
#split, list for words
#declare last letter in for loop, ensure its a vowel
#iterate to create dictionary of last letters: count
#-----
#use max dictionary method to find largest count
#else return greatest
#-----
#result = str, one letter
# counts the most common vowel that words end
