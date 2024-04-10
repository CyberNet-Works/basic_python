def get_maximal(lst):
    maximal = max(set(lst), key = lst.count)
    if lst.count(maximal) > len(lst) // 2:
        return f'Maximal is {maximal}'
    else:
        return f'No Maximal.  Mode *{maximal}* is {int(lst.count(maximal) / len(lst) * 100)}% of list lenth {len(lst)}'

lst = [1,2,2,2,2,3,3,3,3,]

result = get_maximal(lst)
print(result)