def required_fuel(kms):

    total_required_fuel = kms * 10
    
    
    if kms <= 10:
        extra_fuel = 0
    else:
        extra_fuel = total_required_fuel - 100


    return total_required_fuel, extra_fuel

kms = int(input())
result = required_fuel(kms)
print(result)


