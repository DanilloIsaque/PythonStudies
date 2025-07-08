'''Considere que voce deve aplicar um aumento percentual a todos os preções que estão em uma lista.
Escreva um programa que leia essa lista do teclado. Os valores devem ser lidos enquanto não for
digitado zero. Na sequência, leia a porcentagem de aumento.
Em seguida, usando List Comprehension, faça a aplicação desse aumento a todos os valores e mostre na tela'''

try:
    precos = []
    print('Forneça os preços para a lista. Zero para terminar')
    preco = float(input('digite um valor real: '))
    while preco !=0:
        precos.append(preco)
        preco = float(input('digite um valor real: '))

    print('Os preços são esses: ')
    print(precos)

    aumento = float(input('Digite a porcentagem de aumento: '))
    novosPrecos = [valor * (1 + aumento/100) for valor in precos if valor < 100]
    for valor in novosPrecos:
        print(f'{valor:.2f}')

    print('Fim')
except ValueError:
    print('Valor inválido')
