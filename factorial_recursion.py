def factorial(n):
    
    if n == 1:
        return 1

    return factorial(n - 1) * n



number = int(input())

print(factorial(number))