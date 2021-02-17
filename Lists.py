listaExterno = []

def interageLista(comandoString,valor1,valor2):
    global listaExterno
    if comandoString == 'insert':
        listaExterno.insert(int(valor1),int(valor2))
    if comandoString == 'append':
        listaExterno.append(int(valor1))
    if comandoString == 'remove':
        listaExterno.remove(int(valor1))
    if comandoString == 'sort':
        listaExterno.sort()
    if comandoString == 'pop':
        listaExterno.pop()
    if comandoString == 'reverse':
        listaExterno.reverse()
    if comandoString == 'print':
        print(listaExterno)

if __name__ == '__main__':
    N = int(input())
    while True:
        try:
            comandoLista = input()
            
            comandoValores = comandoLista.split(' ') 
            
            if len(comandoValores) > 2:
                interageLista(comandoValores[0],comandoValores[1],comandoValores[2])
            elif len(comandoValores) > 1:
                interageLista(comandoValores[0],comandoValores[1],'')
            else:
                interageLista(comandoValores[0],'','')
        except (EOFError):
            break
        
