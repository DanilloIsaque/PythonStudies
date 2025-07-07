'''programa q ue se mantem em laço lendo numeros inteiros até que seja digitado 0.
Todos os valores digitados, exceto o 0, devem ser gravados em um arquivo em disco, um por linha. usar
o método .write()'''

try:
    #se o arquivo já existe, ele é sobrescrito
    arq = open('saida_ex_1.txt', 'w')  #w indica que estamos abrindo o arquivo para gravação

    x = int(input('Digite um inteiro: '))

    while x !=0:
        arq.write(f'{x}\n') # só aceita string
        x = int(input('Digite um inteiro: '))

    arq.close() # garante q o arquivo seja finalizado e fechado e garantir que não seja perdido

except ValueError :
    print('Digite apenas valores inteiros')
