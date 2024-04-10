import datetime

def calculate_days_between(date1, date2):

    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

    delta = date2 - date1

    return delta.days
    
# take user input
date1 = input()
date2 = input()

# call the function
print(calculate_days_between(date1, date2))