def find_prime(n):
    prime = True
    for x in range(2, n):
        if n % x == 0:
            prime = False
    return prime

def largest_prime_factor(num):
    primes = []
    for x in range(2, num + 1):
        if num % x == 0 and find_prime(x):
            primes.append(x)
    return primes[-1]
    


# take user input
user_input = int(input())

# call the function
print(largest_prime_factor(user_input))