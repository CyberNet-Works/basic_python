def is_sum_present(num_list, target_sum):
    for num1 in num_list:
        for num2 in num_list:
            if num1 != num2 and num1 + num2 == target_sum:
                return True
    return False

# take user input
num_list = list(map(int, input().split()))
target_sum = int(input())

# call the function
print(is_sum_present(num_list, target_sum))


'''
Sum of Two Numbers Equal to Given Number in List
Medium
Problem Description
Write a program to check if the sum of any two elements in a list is equal to a given number.

Define a function named is_sum_present() that takes two arguments - a list of numbers named num_list and a number named target_sum.
Inside the function, check for each pair of numbers in the list. If the sum of any pair is equal to target_sum, return True. Otherwise, return False.
'''