#find maximal with Boyer-Moore Voting Algorithm
def findMajorityElement(nums):
    candidate = None     # Step 1: Find a candidate
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    count = sum(1 for num in nums if num == candidate)     # Step 2: Verify the candidate 
    if count > len(nums) // 2:
        return candidate
    else:
        return None  # No majority element


#remove vowels from string
def remove_vowels(s):
    result = ""
    for char in s:
        if char not in "AEIOUaeiou":
            result += char
    print(result)

remove_vowels("A quick brown fox jumps over the lazy dog")



#count vowels and consonants:#count vowels, and consonants
#len of string - len of vowels = consonants




def count_v_and_c(s):
    vowels = 0
    consonants = 0
    for x in s:
        if x in "AEIOUaeiou":
            vowels += 1
        elif x in " ,.!@#$%^&*(*()_+|)":
            continue
        else:
            consonants +=1
    print(f'Vowels: {vowels}')
    print(f'Consonants: {consonants}')


string = 'A quick brown fox jumps over the lazy dog'

count_v_and_c(string)


#version 2 s = "A quick brown fox jumps over the lazy dog'
vowels = sum(1 for x in s if x.lower() in "aeiou")
consonants = sum(1 for x in s if x.lower() not in "aeiou" and x.isalpha())

print(f"Vowels: {vowels}, Consonants: {consonants}")






# find maximal by sorting short version
def find_majorty(nums):
    nums.sort()
    return nums[len(nums) // 2]

#find maximal by sorting long version with validation that there IS a majority element.
def find_majority(nums):
    nums.sort()
    candidate = nums[len(nums) // 2]
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None  # Indicates no majority element exists


#Finding maximal by checking if each list item is greater than the length of the whole list.
def find_majority_element(num_list):
    for num in numbers:
        
        count = numbers.count(num)       
        if count > len(numbers) // 2:
            return num


# given list with majority element
numbers = [1, 7, 8, 7, 7, 7]

# call the method with list as an argument
result = find_majority_element(numbers)
print(result)


#Find maximal by list count, saving list item and count value in dictionary loop.  
#Choosing the highest count,
#then iterating for highest count

numbers = [1, 7, 8, 7, 7, 7]
count = 0
x = 0
dict={}

for key in numbers:
    key_count = numbers.count(key)
    dict[key] = key_count

highest_count = max(dict.values())
print([key for key, value in dict.items() if value == highest_count])

#COUNT VOWELS
s = "A quick brown fox jumps over the lazy dog"
vowels = sum(1 for x in s if x.lower() in "aeiou")
consonants = sum(1 for x in s if x.lower() not in "aeiou" and x.isalpha())

print(f"Vowels: {vowels}, Consonants: {consonants}")


string = "something happened today"

vowels = sum(1 for char in string if char.lower() in "aeiou")
consonants = sum(1 for char in string if char.lower() not in "aeiou" and char.isalpha())

print(vowels)
print(consonants)



#sum all numbers in a list
'''numbers = [1,2,3,4,5,6,7,8,9,10]
last_num = 0
for num in numbers:
    num = num + last_num
    last_num = num
    
print(last_num)
print(sum(numbers))

#Replace letters in strings
string = "Here is a string"
'''

def replace(string, original, replacement):
    result = ""

    for char in string:
        if char not in replacement:
            result += char
        else:
            result += replacement

print(replace("Holy mary mother of God.", "ly","pe"))            



#find maximal with Boyer-Moore Voting Algorithm


#Count consonants and vowels of a string
def count_chars(string):
    vowels = sum(1 for char in string if char.lower() in "aeiou")

    consonants = sum(1 for char in string if char.lower() not in "aeiou" and char.isalpha())
    
    print(f'Vowels: {vowels}\nConsonants: {consonants}')

string = "A quick brown fox jumps over the lazy dog"
count_chars(string)


def check_capital(string): #make the function, name it accordingly
    counter = 0 #initialize counter
    for capitals in string: #finite loop to iterate letters called capitals 
        ascii_value = ord(char)
        # Check if the ASCII value is within the specified range
        if lower_bound <= ascii_value <= upper_bound:
            # If it is, increment the count
            count += 1



string = "The Sun emits UV light"

print(check_capital(string))



#sum odd factors:
def get_factors(number):
    factors = []
    for factor_candidate in range(1, int((number / 2) + 1)):
            if number % factor_candidate == 0 and factor_candidate % 2 != 0:
                factors.append(factor_candidate)
    return sum(factors)

num_to_factor = 18
print(get_factors(num_to_factor))

#sum odd factors comprehension list:
def get_factors(number):
    # Convert number to integer in case it's a float
    number = int(number)
    # List comprehension that iterates through possible factors and checks your conditions
    factors = [factor_candidate for factor_candidate in range(1, int(number / 2) + 1) 
               if number % factor_candidate == 0 and factor_candidate % 2 != 0]
    return sum(factors)

num_to_factor = 18
print(get_factors(num_to_factor))


#The Number of Capital Letters in the String
def count_capital_chars(string):
    UPPERLIST = []
    for letter in string:
        if letter.isupper():
            UPPERLIST.append(letter)
    return len(UPPERLIST)

string = "The Sun emits UV light"
print(count_capital_chars(string))

#The number of Capital Letters in the string

string = "The Sun emits UV light"
print(count_capital_chars(string))

UPPERLIST = []
UPPERLIST = [UPPERLIST.append(letter) for letter in string if letter.isupper()]


#convert list to string:
def convert_list_to_string(list1):
    for char in list1:
        sentence = ' '.join(list1)
        return sentence

list1 = ['Hello', 'world', 'from', 'Python']

print(convert_list_to_string(list1))

#convert list to string - more pythonic (for loop is unnecessary)
def convert_list_to_string(list1):
    return ' '.join(list1)

list1 = ['Hello', 'world', 'from', 'Python']
print(convert_list_to_string(list1))

#convert list to eschew words starting with consonants:# return items starting without vowels, for list size n.


list1 = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

def convert(list1):
    list2 = []
    vowels = "aeiou"
    for word in list1:
        if word[0].lower() not in vowels:
            list2.append(word)
    return list2

print(convert(list1))

#list comprehension version:
list1 = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

def convert(list1):
    vowels = "aeiou"
    return [word for word in list1 if word[0].lower() not in vowels]

print(convert(list1))


