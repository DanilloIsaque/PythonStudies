#função parImpar

def par(a):
    return "par" if a % 2 == 0 else "ímpar"


par(int(input()))

#somar valores de uma lista
lista = [1,2,3,4,5]
resultado = 0

print(sum(lista))

for i in lista:
    resultado = resultado + i

print(resultado)

#elementos de uma lista maior que 10
lista2 = [1,20,30,9,5,6,70,80]
cont = 0

for i in lista2:
    if(i>10):
        cont +=1

print(cont)

#dicionario
pessoa = {
    "nome":"Danillo",
    "idade":21
}


#caso a chave n exista, print(pessoa.get("nome", "Desconhecido"))

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")



#contagem de 1 ao 10
for i in range(1,11):
    print(i)


#input nome e idade
nome = input("Digite seu nome:")
idade= input("Digite sua idade:")

print(f"Seu nome é {nome} e vc tem {idade} anos")