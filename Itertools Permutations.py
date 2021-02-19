from itertools import permutations

if __name__ == "__main__":
    
    x = list(map(str, input().split()))
    
    s,n = x[0],x[1]
    
    for _ in sorted(list(permutations(s,int(n)))):
        print(''.join(_))
