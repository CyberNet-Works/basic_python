#Flattening to a 1D List
def flatten_list(list_of_lists):
    new = []
    for sub in list_of_lists:
        if isinstance(sub, list):
            new += sub

    return new

# initialize list of lists
list_of_lists = []

# take user inputs 
# for number of sublists
n = int(input())

# for sublists
for _ in range(n):
    sublist = list(map(int, input().split()))
    list_of_lists.append(sublist)

# call the function
print(flatten_list(list_of_lists))

'''
Problem Description
Write a program to flatten a list of lists into a single list.

Define a function named flatten_list() that takes a single argument list_of_lists.
Inside the function, create a new one dimensional list that contains all the elements from the sublists.
Return the newly created list.
The input format is:

number_of_lists_in_nested_list(n)
list_1
list_2
...
list_n
Example
Test Input

2
[0, 1, 2, 3]
[4, 5]
Expected Output

[0, 1, 2, 3, 4, 5]


'''