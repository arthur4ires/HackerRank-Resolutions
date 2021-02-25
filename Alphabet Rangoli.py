
def getMedian(value):
    
    if value % 2 == 0:
        return int(value/2)
    else:
        return int((value + 1)/2)
    
def print_rangoli(sizeNumber):
    
    baseNumber = 97
    horizontalValue = 0
    
    verticalLine =  (sizeNumber * 2) - 1 
    horizontalLine = (sizeNumber * 4) - 3
    
    for a in range(verticalLine):
        a += 1

        if getMedian(verticalLine) > a:
            chrVar = int(verticalLine/2)
        else:
            chrVar = int(verticalLine/2)
        
        abcValue = chr(baseNumber + (chrVar))

        if (int(horizontalValue/4)) > 0:
            abcValue = chr(baseNumber + (chrVar) - 1) + "-" + abcValue + "-" + chr(baseNumber + (chrVar) - 1) 

        print(abcValue.center(horizontalLine-horizontalValue,'-'))

        if getMedian(verticalLine) > a:
            horizontalValue += 4
        else:
            horizontalValue -= 4
       
if __name__ == '__main__':
    #n = int(input())
    n = 5
    print_rangoli(n)
