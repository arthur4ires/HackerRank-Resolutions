def getMedian(number):
    if number%2 != 0:
        return (number - 1)/2
    
def generateWelcome(N,M):
    
    centerInfo = ".|."
    centerPrint = "WELCOME"
    a = 0
    b = 1
    
    for x in range(N): #every line
        
        if getMedian(N) == x:
            
            numberResult = int((M-len(centerPrint))/2)
            
            print("-" * numberResult + centerPrint + "-" * numberResult)
            
        if getMedian(N) > x:
                       
            newItem = centerInfo * (a+b)
                  
            a += 1
            b += 1
            
            print(newItem.center((M),"-"))
            
        if getMedian(N) < x:
            
            a -= 1
            b -= 1
            
            newItem = centerInfo * (a+b)      

            
            print(newItem.center((M),"-"))
        
if __name__ == "__main__":
    N,M = map(int, input().split(' '))

    generateWelcome(N,M)
    
