from itertools import product

if __name__ == "__main__":
    
    x = map(int,(input().split()))
    y = map(int,(input().split()))
    
    listProduts = list(product(x,y))
    
    print(' '.join(str(v) for v in listProduts))
