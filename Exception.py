if __name__ == "__main__":
    N =  int(input())
   
    for _ in range(N):
        try:
            valueInput = list(map(int, input().split(' ')))
            print(valueInput[0]//valueInput[1])
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)
            
