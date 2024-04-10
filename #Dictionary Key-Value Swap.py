#Dictionary Key-Value Swap
def swap_dict(dict):
    new_dict = {}

    for key, value in dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
        
    return new_dict



# take user input
dict = eval(input())

# call the function
print(swap_dict(dict))


'''
Dictionary Key-Value Swap
Medium
Problem Description
Write a program to swap the keys and values of a dictionary.

Define a function named swap_dict() with a single argument (dictionary).
Inside the function, reverse the keys and values of the given dictionary. If a value is found more than once, group those keys together in a list.
Example
Test Input

{'Pizza': 'Food', 'Pasta': 'Food', 'Water': 'Drink', 'Coke': 'Drink'}
Expected Output

{'Food': ['Pizza', 'Pasta'], 'Drink': ['Water', 'Coke']}
Reason: The value Food is more than once in the test input so the keys of Food are kept inside a List. ['Pizza','Pasta'].

'''