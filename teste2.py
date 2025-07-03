import math

#Função que verifica se um número é primo
def ehPrimo(num):
    if num <= 1:
        return False  #
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(ehPrimo(int(input("Digite um número: "))))

#filtrar e somar pares
numeros = [10, 15, 22, 33, 40, 7, 9]

print(sorted(numeros))
soma=0
for i in numeros:
    if i%2==0:
      soma += i
print(soma)

#soma = sum(i for i in numeros if i % 2 == 0)

#Crie um dicionário com 3 alunos, contendo nome e nota.
# Depois, imprima o nome do aluno com a maior nota.

pessoas = [
    {"nome": "Danillo", "nota": 10},
    {"nome": "Isaque", "nota": 3},
    {"nome": "Brito", "nota": 4}
]


maior = pessoas[0]
for pessoa in pessoas:
    if pessoa["nota"] > maior["nota"]:
        maior = pessoa

print(f"O aluno com a maior nota é {maior['nome']} ({maior['nota']})")


#alunos = {
 #   "Danillo": 8.5,
 #   "Lucas": 7.0,
  #  "Ana": 9.2
#}

#melhor_aluno = max(alunos, key=alunos.get)
#print(f"O aluno com a maior nota é {melhor_aluno} ({alunos[melhor_aluno]})")

#Peça para o usuário digitar 3 notas (float) e imprima a média com 2 casas decimais.

nota1 = (float(input("Digite a primeira nota: ")))
nota2 = (float(input("Digite a segunda nota: ")))
nota3 = (float(input("Digite a terceira nota: ")))

media = (nota1 + nota2 + nota3)/3

print(f"A média é {media:.2f}")

print(type(media))

print(math.sqrt(49))



