def printInt(n):
    numberPrint = ""
    for x in range(n):
        if (x != n and x != 0):
            numberPrint = numberPrint + str(x)
    
    print(numberPrint + str(n))

if __name__ == '__main__':
    n = int(input())
    printInt(n)
