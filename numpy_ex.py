if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
        
    higher = -9999
    prev = 0
    
    for number in arr:
        if number >= higher:
            higher = number
        else:
            prev = number
    print(prev)
