def filter_dict_values(mixed_dict, k):
    newdict = {}

    for key, value in mixed_dict.items():
#        print(f"{key} ! {value} ! {k}")
        if isinstance(value, str) or value > k:
            newdict[key] = value

    return newdict

# take user input
user_dict = eval(input())
user_k = int(input())

# call the function
print(filter_dict_values(user_dict, user_k))