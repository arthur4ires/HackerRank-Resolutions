"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

ord('a') -> 97
chr(97) -> a
"""

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
        
        if getMedian(verticalLine) > a:
            chrVar = int(verticalLine/2)
        else:
            chrVar = int(verticalLine/2)
            
        print(chr(baseNumber + (chrVar)).center((horizontalLine-horizontalValue),'-'))
        
        print(horizontalValue)
        
        if getMedian(verticalLine) > a:
            horizontalValue += 4
        else:
            horizontalValue -= 4 
       
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
