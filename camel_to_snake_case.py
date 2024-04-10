def camel_to_snake_case(string):
    result = ""

    for char in string:
        if char.isupper():
            result += char.replace(char,f"_{char}")
        else:
            result += char
    result = result.lower()
    return result

string = input()
result = camel_to_snake_case(string)
print(result)


#camelCase -> snake_case
#make it lowercase.  if char.isupper():