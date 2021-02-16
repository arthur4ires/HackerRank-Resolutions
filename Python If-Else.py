#!/bin/python3

def numberVal(number):
    if (number <= 3):
        print("Weird")
    elif (number >= 2 and number <= 4):
        print("Not Weird")
    elif (number >= 6 and number <= 20):
        print("Weird")
    elif (number > 20 and number%2 == 0):
        print("Not Weird")
    elif (number%2 != 0):
        print("Weird")
        
    

if __name__ == '__main__':
    n = int(input().strip())
    numberVal(n)
    exit()
