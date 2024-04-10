# if n is a power of 3, return true
'''
def check_n():
    n = input("Please enter N: ")
    try:
        n = int(n)
        cube_root = n ** (1 / 3)
        if cube_root == int(cube_root):
            print(True)
        else:
            print(False)
    except ValueError:
        try:
            float_n = float(n)
            if float_n != int(float_n):
                raise ValueError("Input must be an integer or an integer representation of a perfect cube.")
            print(False)
        except ValueError as e:
            print(e)

check_n()



'''
def is_power_of_3(n):
    while n % 3 == 0:
        n //= 3
    return n == 1

while True:
    try:
        n = int(input("Please enter N: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")
'''
y = n ** 3
z = int(n ** (1/3))
print(y)
print(z)
print(is_power_of_3(n))



n = input("Please enter N: ")
n = int(n)
y = n ** 3
z = int(n ** (1/3))
print(y)
print(z)

           
def check_n():

    n = input("Please enter N")
    y = n ** 3
    try:
        y = int(y)
        return True
        print("True")
    except ValueError:
        return False
        print("False")
check_n()
            
'''