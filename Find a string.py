def count_substring(string, sub_string):

    numberSub = 0
    numberCount = 0
    
    while True:
            
        if (numberSub + len(sub_string)) > len(string):
            break 
             
        if string[numberSub:(numberSub+len(sub_string))] in sub_string:
            numberCount += 1
        
        numberSub += 1
    
    return numberCount

