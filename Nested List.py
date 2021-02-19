def getIndexList(listIndex,valueIndex):
    
    for x,y in enumerate(listIndex):

        if y == listIndex[valueIndex]:
            return x

def minValueArray(nameList, scoreList):
    
    global valueInf
    
    for x in range(len(nameList)): 
        
        minScore = scoreList.index(min(scoreList))
        
        if valueInf != scoreList[minScore] and x != 0:
            break;
        
        valueInf = scoreList[minScore]
        
        listMin.append(nameList[minScore])
        
        scoreList.remove(scoreList[minScore])
        del nameList[minScore]
        
    for y in sorted(listMin):
        print(y)
    
    return True
    
    
if __name__ == '__main__':
    nameList = []
    scoreList = []
    listMin = []
    valueInf = 0
    
    n = int(input())
    
    for _ in range(n):
        
        name = input()
        score = float(input())
        nameList.append(name)
        scoreList.append(score)
    
    while True:

        if n == len(scoreList):
            
            while True:
                oldValue = scoreList[scoreList.index(min(scoreList))]
                
                indexValue = getIndexList(scoreList, scoreList.index(min(scoreList)))
                scoreList.remove(scoreList[scoreList.index(min(scoreList))])
                
                del nameList[indexValue]
                
                if oldValue != scoreList[scoreList.index(min(scoreList))]:
                    break
        else:
            if minValueArray(nameList, scoreList) == True:
                break
