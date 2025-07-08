from random import randint

def saudacao(nome, mensagem ='Olá,'): #valor padrão
    print(mensagem,nome)

def exibehifens():
    print('------')

def lerinteiro():
    x = int(input("Digite um valor inteiro: "))
    return x

def carregarlista(qtd, a, b):
    '''carrega uma lista de números inteiros aleatorios'''
    l = []
    for i in range(qtd):
         l.append(randint(a,b))
    return l

#empacotamento de parametros
def somatoria(*dados):
    r =0
    for i in dados:
        r +=i
    return r

def montasaida(*valores, separador = ', ' ):
    saida = separador.join(valores) # separador é o ponto de partida da construção da concatenação de strings
    return saida

def calculo(a,b,c):
    return (a+b)/c

def funcao1():
    print('temos dentro da função: ', tst1, tst2) # escopo global

def funcao2():
    tst1 = 100
    tst2 = 200
    print('temos dentro da função: ', tst1, tst2) # escopo local

#funçao recursiva
def fatorial(n):
    if n<=1:
        return n
    else:
        return  n * fatorial(n-1) #fica no looping


#lambda
def mais2(n):
     return n + 2

def quadrado(a):
    return a**2

tst1 = 10# escopo global
tst2 = 10
saudacao('Danillo')
saudacao('Danillo', 'Bom dia,')
lista = [10,20,30,40]
for valor in lista:
    print(valor)
    exibehifens()

valor= lerinteiro()
print(f'o valor é {valor}')
min = int(input('Digite o limite minimo: '))
max = int(input('Digite o limite maximo: '))
qtd = int(input('Digite quantidade desejada: '))
valores = carregarlista(qtd,min,max)
print(f'valores da lista: {valores}')

print(somatoria(1,2,3,4))
print(montasaida('maça','laranja', 'mamão', 'morango'))
print(montasaida('maça','laranja', 'mamão', 'morango', separador='...'))

li = [2,4,2]
tup = (2,4,2)
#print(calculo(li))
# a quantidade de argumento tem q condizer com a quantidade de valores que a função precisa receber
print(calculo(*li))
print(calculo(*tup))

fator = int(input('Digite o numero inteiro para fatorial: '))
f = fatorial(fator)
print(f'o fatorial de {fator} é {f}')

(lambda x: x+2) (10)

(lambda  x, y, z: (x + y) / z) (350,50,20)

L = [8,5,3,9,7,2]
L2 = map(quadrado,L)

for x in L2:
    print(x)

#na função lambda
L3 = map((lambda x: x**3), L)
for x in L3:
    print(x)