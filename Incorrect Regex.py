import re 

def validateRegex(regexValue):
    try:
        re.match(regexValue,':D')
        return True
    except:
        return False

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        print(validateRegex(input()))
        
