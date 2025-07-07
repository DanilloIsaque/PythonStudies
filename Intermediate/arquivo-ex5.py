'''Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário e ao final exibindo-os na tela. A figura 11.1 mostra do lado esquerdo a natureza dos dados que serão lidos e do lado direito mostra o formato do arquivo.
Esse formato é conhecido como CSV. Arquivos CSV são muito usados em diversas áreas da computação, em especial em Análise de Dados. O que caracteriza um arquivo CSV é que cada linha tem um conjunto de dados de alguma forma relacionados e separados por um caractere delimitador.
No arquivo deste exercício o delimitador é um ponto-e-vírgula ";"
Neste caso, cada linha tem: código de produto (int), a quantidade em estoque (int), preço (float). Use o'''

estoque = {}
for linha in open('entrada_ex5.txt', 'r'):
    lst= linha.rstrip().split(';') # remover cada \n que vem em cada linha
    print(lst)
    # print(l, end='...') vai exibir cada linha com os pontos
    cod = int(lst[0])
    qtd = int(lst[1])
    pcUnit = float(lst[2])
    estoque[cod] = (qtd,pcUnit)


print('\nValores carregados no dicionário\n')
print(estoque)
print('\nExibição em formato de tabela\n')
totGeral =0
for cod, dados in estoque.items():
    tot = dados[0] * dados[1]
    totGeral += tot
    print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}') # gasta 6 posicoes na tela, sendo duas decimais

print(' ' * 24, f'{totGeral:8.2f}')



print('\nFim')