def stringValidator(string):
    isAlnum = False
    isAlpha = False
    isDigit = False
    isLower = False
    isUpper = False
          
    for subString in string:
        if subString.isalnum() == True:
            isAlnum = True
        if subString.isdigit() == True:
            isDigit = True
        if subString.isalpha() == True:
            isAlpha = True
        if subString.islower() == True:
            isLower = True
        if subString.isupper() == True:
            isUpper = True
    
    print(isAlnum)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)

if __name__ == '__main__':
    s = input()
    stringValidator(s)
