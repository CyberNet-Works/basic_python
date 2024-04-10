#maximal boyer moore count voting algorithm

def maximal(list):
    for candidate in list:
        if list.count(candidate) > len(list) // 2:
            return candidate
    
list = [1,2,2,3,3,3,3,3]

print(maximal(list))


#remove vowels from string

def remove_vowels(string1):
    newstring = ""
    for char in string1:
        if char.lower() in "aeiou":
            continue
        else:
            newstring += char
    return newstring

#thestring = "This is a test from the Emergency broadcasting system"

#print(remove_vowels(thestring))

#sum all numbers in a list
#lista = [1,2,3,4,5,6,7,8,9,10]

#lista_sum = sum(lista)

#print(lista_sum)

#sum odd factors: 1) find factors, sum them.

def sum_odd_factors(number): #function to sum odd factors
    total_odd_factors = 0

    for factor in range(1, int(number / 2) + 1):  #iterating for factors from 1 to the number including the number.
        if number % factor == 0 and number % 2 != 0: #checking for factors and odd numbers
            total_odd_factors += factor #add sum the factor into a variable  
    return total_odd_factors

#thenewnumber = 9
#print(sum_odd_factors(thenewnumber))

#The Number of Capital Letters in the String
def count_caps(string2):
    counter = 0
    for char in string2:
        if char.isupper():
            counter += 1
    return counter

#string2 = "THE DOG is lying and does not want to go for a walk but it will PISS on my FLOOR."       
#print(count_caps(string2))

#convert list to string letter by letter:
#string3 = list(string2)
#print(string3)


#convert list to string word by word:
def list_convert_to_words(stringb):
    neword = ' '.join(stringb)
    neword.append(listb)
    return listb

#print(list_convert_to_words(string2))

#copy only words starting with consonants in a list to a new list:
'''  THE BELOW USES AN UNNESSESSARY ELSE STATEMENT THAT MAKES IT IMPOSSIBLE TO CONVERT TO A COMPREHENSION LIST.
def copy_consonants(fruits):
    new_list = []
    for word in fruits:
        if word[0].lower().startswith(("a","e","i","o","u")):
            continue
        else:
            new_list.append(word)
    return new_list

fruits = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']
print(copy_consonants(fruits))
'''
'''****THIS IS THE CORRECT VERSION****'''
def new_listf(fruits):        
    new_list = []  # Initialize an empty list
    for word in fruits:
        # Check if the word does not start with a vowel
        if not word[0].lower().startswith(("a", "e", "i", "o", "u")):
            new_list.append(word)  # Append to new_list if it starts with a consonant
    return new_list

#fruits = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

# This will print the new list containing words that start with a consonant

#print(new_listf(fruits))

#CORRECT list comprehension:
def new_listf(fruits):    
    new_list = [word for word in fruits if not word[0].lower().startswith(("a", "e", "i", "o", "u"))]
    return new_list


#fruits = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

# This will print the new list containing words that start with a consonant

#print(new_listf(fruits))


####increase values in a dictionary: ###  Long hand:
def incrementer(player_scores):
    incremented_scores = {}  # Initialize an empty dictionary
    #    incremented_scores = {key: value + 1 for key, value in player_scores.items()}
    for key, value in player_scores.items():
        incremented_scores[key] = value + 1  # Increment the score and add it to the new dictionary
    return incremented_scores  # Return the updated dictionary

# Define the original dictionary
player_scores = {
    'Cody': 50,
    'Jack': 57,
    'Seth': 59,
    'Roman': 67,
}

# Call the function and print the incremented scores
#print(incrementer(player_scores))


#add any number of parameters:
def adder(*args):
    summed = sum(args)
    return summed

#print(adder(1, 2, 3, 4, 5))

####Find middle letter in a list:

def middle_letter_func(stringvar):
    middle_letter = stringvar[len(stringvar) // 2]
    return middle_letter

#stringa = "hello"

#print(middle_letter_func(stringa))

#print(middle_letter_func(stringa))


###comprehension list for getting list of indices of capital letters in a string:
def return_uppercase_indices(string):
    # Use enumerate to get both index and letter, and check if the letter is uppercase
    upper_indices = [index for index, letter in enumerate(string) if letter.isupper()]
    return upper_indices

#stringa = "heLLo"
#print(return_uppercase_indices(stringa))

#long form of getting indices of a string:
def return_uppercase_indices(string):
    upper_indices = []  # Initialize an empty list to store indexes
    for index, letter in enumerate(string):  # Use enumerate to get both index and letter
        if letter.isupper():  # Check if the letter is uppercase
            upper_indices.append(index)  # Append the index to the list if condition is met
    return upper_indices  # Return the list of indexes

#stringa = "heLLo"
#print(return_uppercase_indices(stringa))


#sort words alphabetically
def sort_words_alphabetically(input_string):
    # Split the string into words
    words = input_string.split()
    # Sort the list of words alphabetically
    sorted_words = sorted(words)
    # Join the sorted words with a newline character to have one word per line
    return '\n'.join(sorted_words)

# Example usage
input_string = "python is easy"
sorted_words_string = sort_words_alphabetically(input_string)
print(sorted_words_string)


#
# define a function to find the before and after of a given number
def before_and_after(n):

    # decrement the number by 1 to find the before number
    before = n - 1

    # increment the number by 1 to find the after number
    after = n + 1

    # return the tuple of before, n and after
    return (before, n, after)


# call the function
result = before_and_after(5)
print(result)
