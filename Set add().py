def setReturn(N):
    setList = set()
    
    for _ in range(N):
        setList.add(input())
    
    return len(setList)
if __name__ == "__main__":
    print(setReturn(int(input())))
        
