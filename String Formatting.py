def print_formatted(number):
    
    #na força do ódio essa merda

    for x in range(1,number+1):
        n = number.bit_length()
        print(f"{x:{n}d} {x:{n}o} {x:{n}X} {x:{n}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
