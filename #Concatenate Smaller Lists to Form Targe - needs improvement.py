#Concatenate Smaller Lists to Form Target List
def can_form_target(list_of_lists, target_list):
    target_list = sorted(target_list)

    max_i = len(list_of_lists)
    result = []

    for i in range(0,max_i):
        for y in list_of_lists:
            result += list_of_lists[i]

    result = sorted(list(set(result)))
    
    return result == target_list


# take user inputs
user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
user_target_list = list(map(int, input().split()))

# call the function
print(can_form_target(user_list_of_lists, user_target_list))


'''
Concatenate Smaller Lists to Form Target List
Medium
Problem Description
Write a program that checks if the target list can be formed by only concatenating given smaller lists.

Define a function named can_form_target() with two arguments: list_of_lists (list of lists of integers) and target_list (list of integers).
Inside the function, concatenate all the lists inside list_of_lists and compare with the target_list. Return True if they are the same (ignoring order), else return False.

'''