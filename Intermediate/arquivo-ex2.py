''' escreva um programa que permaneça em laço lendo numeros reais até que seja
digitado 0. Todos os valores digitados, exceto zero, devem ser gravados em um arquivo em disco,
um por linha, com tres casa decimais.
usar o método .writeLines()'''

lista = []


try:
    x = float(input('Digite um número real: '))
    while x != 0:
        lista.append(f'{x:.3f}\n')
        x = float(input('Digite um número real: '))

    arq = open('saida_ex_2.txt', 'w')
    arq.writelines(lista)
    arq.close()
except ValueError:
    print('Digite apenas valores reais')