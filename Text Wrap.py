import textwrap

def wrap(string, max_width):
    listResults = []
    
    for x in range(0, len(string), max_width):
        listResults.append(string[x:x+max_width])
                    
    return '\n'.join(listResults)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
