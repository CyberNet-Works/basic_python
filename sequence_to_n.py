if __name__ == '__main__':
    
    def recursion(n):
        length = len(n)
        result = 0

        for position in range(n + 1):
            print(position)
        
        return result

    n = int(input())
    print(recursion(n))
    




