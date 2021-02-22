def countUnion(C1,C2): 
    return len(C2.union(C1))

if __name__ == "__main__":
    N1 = int(input())
    C1 =  set(map(int , input().split(' ')
    ))
    N2 = int(input())
    C2 = set(map(int, input().split(' ')))
    print(countUnion(C1,C2))
