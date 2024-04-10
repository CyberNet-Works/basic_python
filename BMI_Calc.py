BMI Calc
# Complete the code below

# define a function
def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    if bmi > 30:
        return "Obese"
    elif bmi > 25:
        return "Overweight"
    elif bmi > 18.5:
        return "Normal Weight"
    else:
        return "Underweight"


# call the function
weight = float(input())
height = float(input())
result = calculate_bmi(weight, height)
print(result)