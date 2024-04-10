if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = arr
    def get_second_place(arr1):
        
        first_place = max(arr1)
        
        for num in arr1:
            if num == first_place():
                first_place.pop(num)
        second_place = max(arr1)

        return second_place
        
    result = get_second_place(arr1)
    
    print(result)
