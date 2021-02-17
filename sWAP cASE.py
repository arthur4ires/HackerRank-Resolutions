def swap_case(nomeString):
    novaString = ''
    
    for a in nomeString:
        if a.isupper() == True:
            novaString += a.lower()
        else:
            novaString += a.upper()
 
    return novaString

