def average(array):
    
    valueMedian = 0.0
    newArray = list(dict.fromkeys(array))
    
    valueMedian = sum(newArray)/len(newArray)
    
    return valueMedian

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
