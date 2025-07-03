x =10
y = 8

print (f'o valor de x é {x}') if x>= y else print(y) #else é obrigatório


codigos =[103,117,121,135,161,189,200,204,216]
lista = []

for codigo in codigos:
    if 120 <= codigo and codigo <= 200:
        lista.append(codigo)

    print(f' codgios filtrados :{lista}')

lista = []

for codigo in codigos:
    lista.append(codigo) if 120 <= codigo <= 200 else 0

    print(f' codigos filtrados :{lista}')


print('\n\n paridade')

z = int(input('digite um inteiro: '))
paridade = 'par' if z%2 ==0 else 'impar'
print(f'o valor de {z} é {paridade}')