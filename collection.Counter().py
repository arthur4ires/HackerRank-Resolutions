def calculateValue(listShoes, sizeShoes):
    
    totalPrice = 0

    for a in listShoes:
        
        if a[0] in sizeShoes:
            sizeShoes.remove(a[0])
            totalPrice += a[1]
    
    return totalPrice
    
if __name__ == "__main__":
    
    numberShoes = int(input())
    sizeShoes = list(map(int, input().split(' ')))
    customerShoes = int(input())
    
    listShoes = []
    
    while True:
        try:
            listShoes.append(list(map(int , input().split())))
        except:
            break;
    
    print(calculateValue(listShoes, sizeShoes))
        
        
