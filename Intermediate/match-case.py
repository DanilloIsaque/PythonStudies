n = -1
while n != 0:
    n = int(input('digite um inteiro: '))
    match n :
        case 1:
             print('você digitou 1')
        case 2:
            print('você digitou 2')
        case 3:
            print('você digitou 3')
        case 4:
             print('você digitou 4')
        case _:
            print(' você digitou outro valor')

print("\n\nfim")