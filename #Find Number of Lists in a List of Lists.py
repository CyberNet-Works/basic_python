#Find Number of Lists in a List of Lists

def count_sublists(list_input):
    count = 0
    for x in list_input:
        if isinstance(x, list):
            count += 1

    return count

# take user input
list_input = eval(input())

# call the function
print(count_sublists(list_input))