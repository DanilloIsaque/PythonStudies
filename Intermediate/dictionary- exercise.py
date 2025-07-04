'''leia do teclado o codgo de um produto e seu preço unitário
o código é string e o preço é real. acrescente o par código:preço em um dicionário
o laço termina quando for fornecido um string vazio para o código. ao final, exibir código e preço, em cada linha'''


produtos ={}
print('Leitura dos dados')
codigo = input(' Digite o código ')

while codigo != '':
    preco = float(input(' Digite o preço: '))
    produtos[codigo] = preco
    codigo = input(' Digite o código')


print("\n\nProdutos")

for cod in produtos.keys():
        print(f'Produto {cod} - R${produtos[cod]:.2f}')