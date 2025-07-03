

try:
    a = int(input('Digite a:'))
    b = int(input('Digite b:'))
    r = a / b
    print(r)
except ZeroDivisionError:
    print ('não é possivel dividir por zero' )
except ValueError :
    print('digite numeros inteiros para a e b')
except:
    print('não é possivel calcular a divisão')
print('fim do programa ')