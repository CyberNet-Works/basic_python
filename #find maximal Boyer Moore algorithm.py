#maximal Boyer Moore Algorithm

def maximal(list):
    for candidate in list:
        counter = list.count(candidate)

        if counter > len(list) // 2:
            return candidate

list = [1,2,3,4,5,6,7,7,7,7,7,7,7,7,]

result = maximal(list)

print(result)