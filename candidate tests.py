def get_maximal(lst):
    maximal = max(set(lst), key = lst.count)
    
    if lst.count(maximal) > len(lst) // 2:
        return maximal
    else:
        return f"No maximal: {len(lst)} elements"

lst = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
result = get_maximal(lst)
print(result)




















