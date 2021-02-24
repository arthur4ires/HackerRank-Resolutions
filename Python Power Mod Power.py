def calcPow(a,b,c = 1):
    if c != 1:
        return pow(a,b,c)
    else:
        return pow(a,b)

if __name__== "__main__":
    a,b,c = int(input()),int(input()), int(input())
    
    print(calcPow(a,b))
    print(calcPow(a,b,c))
