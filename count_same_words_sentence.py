# count number of same words in a sentence

# define a function
def same_word_counter(string):
    string = string.lower()
    string = string.replace("\"","").replace(",","").replace(".","")
    words = string.split()
    counts = {}

    for word in words:
        if word in counts and word.isalpha():
            counts[word] += 1
        else:
            counts[word] = 1
    
    return counts




# call the function
string = input()
result = same_word_counter(string)
print(result)


#output is dictionary
#split string to list
#iterate. put key/word in dictionary with count/value