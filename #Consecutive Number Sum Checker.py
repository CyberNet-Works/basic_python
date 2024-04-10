#Consecutive Number Sum Checker

def check_consecutive_sum(a, n):
    result = 0 #initiate result
    if n - a <= 1: #base case if distance between a and n is 1 or less
        return False  #end of recursion if not True

    for x in range(a, n):   #check from a to n starting at 0
        result += x     #result adds x until n
        if result == n: #if its n, returns True
            return True
    a += 1  #increment 1
    return check_consecutive_sum(a, n)   #recursive function.  We could have moved a+=1 into the function arguments a + 1, n)

# take user input
n = int(input())

# call the function
print(check_consecutive_sum(0, n))


'''
Consecutive Number Sum Checker
Medium
Problem Description
Write a program to check whether a given number can be expressed as a sum of two or more consecutive positive numbers.

For example,

1 + 2 +3 = 6
4 + 5 = 9
Define a function named check_consecutive_sum() with a single argument n.
Inside the function, check whether the number can be expressed as a sum of consecutive numbers.
If the number can be represented as a sum of consecutive numbers, return True and return False otherwise.

'''