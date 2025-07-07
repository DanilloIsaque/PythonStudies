'''escreva um programa que leia um arquivo de entrada, sabendo que esse arquivo
tem um numero inteiro e cada linha. Todos os numeros lidos devem ser mostrado na tela.
mostra também a soma dos valores, a quantidade, amédia aritmética, o menor valor e o maior valor.
usar o método readline()
usar o operador for e iterar sobre ele'''

lista = []
#arqEntrada = open('entrada_ex3.txt','r')
for linha in  open('entrada_ex3.txt','r'):
    lista.append(int(linha))

print(f'{lista}\n')
quantidade = len(lista)
soma = sum(lista)
print(f'Soma dos valores da lista:{soma}\n')
print(f'Quantidade de valores na lista:{quantidade}\n')
if quantidade != 0:
    print(f'Média dos valores da lista:{soma/quantidade:.2f}\n')
print(f'Menor valor da lista:{min(lista)}\n')
print(f'Maior valor da lista:{max(lista)}\n')

