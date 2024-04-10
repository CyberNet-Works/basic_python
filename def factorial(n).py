'''def factorial(n):
    if n == 0:
        return 1

    else:
        return factorial(n -1) * n


n = int(input())
result = factorial(n)

print(result)
'''

#decrementing loop

def factorial(n):
    if n == 0:
        return 1

    else:
        return factorial(n -1) * n

n = int(input())
result = factorial(n)
print(result)