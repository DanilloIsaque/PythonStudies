from random import randint

qtd = int(input('digite a quantidade: '))

while qtd > 50:
    print('valor ínvalido')
    qtd = int(input('digite a quantidade: '))

conjunto = set()
while len(conjunto) < qtd :
        conjunto.add(randint(1,50))
print(conjunto)
print(f'o conjutno tem {len(conjunto)} elementos')
