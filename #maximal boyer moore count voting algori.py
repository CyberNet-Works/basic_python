#maximal boyer moore count voting algorithm
#def maximal(list):
#    for candidate in list:
#        if len(list) % 2 != 0:
#            if list.count(candidate) > len(list) // 2:
#                return candidate
#        else:
#           return "list divisible by 2. Candidate must be > 50%"
#
#list = [1,2,2,3,3,3,]
#
#print(maximal(list))


#remove vowels from string
#def remove_vowels(string):
#    new_string = ""
#    for letter in string:
#        if letter.lower() not in "aeiou":
#            new_string += letter
#    return new_string
#        
#string = "This is a STRING"
#
#print(remove_vowels(string))


#def sum_list(number_list):
#    return sum(number_list)
#    
#
#number_list = [1,2,3,4,5,]
#
#print(sum_list(number_list))

#def get_factors(integer):
#    factorlist = []
#
#    for factor in range(1, integer+1):
#        if number % factor == 0:
#            factorlist.append(factor)
#    return factorlist
#
#number = 12345
#print(find_factors(number))

#def get_odd_factors(integer):
#    odd_factors = []
#    for factor in range(1, integer + 1):
#        if integer % factor == 0 and factor % 2 != 0:
#            odd_factors.append(factor)
#    return odd_factors

#def get_odd_factors_comprehension_list(integer):
#    odd_factors = []
#    odd_factors = [factor for factor in range(1,integer + 1) if integer % factor == 0 and factor % 2 != 0]
#    return odd_factors
#
#number = 9
#print(get_odd_factors_comprehension_list(number))




#def sum_odd_factors(list):
