def is_email_valid(email):
    atposition = 0
    dotposition = 0

    if "@" not in email or "." not in email or email.count("@") > 1:
        return False
        
    for i, char in enumerate(email):
        if char == "@":
            atposition += i
        if char == ".":
            dotposition += i

    if atposition > dotposition or atposition == 0 or dotposition == -2 or dotposition == -1:
        return False

    return True



#   check if there is a character before the @
#   find the @ index, if @ is 0 or [-1] return False
#   find the . index, if it is <= @ index, or if it is -2 or -1, return False.

#   check if @ is before the .
#   check if there is two characters after the .

#   check if there is @ or . in the email, false if no



#   enumerate email to get an index for each character
#   



    return dmail

# take user input
email = input()

# call the function
print(is_email_valid(email))