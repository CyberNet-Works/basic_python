def vowel_repeater(string, n):

    vowels = "aeiou"
    result = ""
    
    for letter in string:
        if letter in vowels:
            result += letter * n
        else:
            result += letter
    return result


string = input()
n = int(input())
result = vowel_repeater(string, n)
print(result)