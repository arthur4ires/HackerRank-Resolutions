def mutate_string(string, position, character):
    novaString =  ''
    
    for x,y in enumerate(string):
        
        if x == position:
            novaString += character
        else:
            novaString += y
            
    return novaString
