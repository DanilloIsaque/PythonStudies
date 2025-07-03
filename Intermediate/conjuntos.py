#set
c1 = {16,8,21,30,41,28}

print(len(c1))

c1 = {16,8,21,30,41,28,8}
print(c1)# não aceitam valores iguais

c1 = {16,8,21,30,41,28,'8'}
print(c1)

c1 = {16,8,21,30,41,28,'8', 8.0}
print(c1)

c2 = set() #conjunto vazio
c3 = {} #dictionary

#c4 = set{4, 9 , 14, 21} ele não permite colocar dados dentro, apenas um elemento (tupla,lista)

c4 = set( [4,9,21,14])


texto = 'teste qualquer'
texto2 = 'Teste qualquer'
c5 = set(texto)
c6 = c5 #criei uma nova variavel e apontei para o mesmo local de memoria que está c5

c6 = set(c5)
print(id(c5))
print(id(c6))

print(texto) # ele separa as letras, não tem ordem e não há repetição de letras

tupla = (16,45,78)
c7 = set(tupla)
c8 = set(texto2)
print(c8)

print('\n\n\n hash')
s1 = 'abcd'
print(hash(s1))
s2 = 'abcd'
print(hash(s2))

# vai dar erro pq a lista não pode fazer parte do conjunto
#c9 = {204,37.3, (9,10,11), [1,2,32], 'abcd'}


cteste= set()
cteste.add(190)
cteste.add(32) #nao tem ordem

cteste.clear() #esvazia

cteste2 = cteste

#id's diferentes
print(id(cteste))
print(id(cteste2))

#operaçoes
cx = {26,32,45,58,63}
cy = {19,34,58,67,82}

print(cx.difference(cy)) # o que estiver no cx e não esta no cy, será retornado

cx.difference_update(cy) # ele já atualiza  o cx
cy.discard(82) # se não existir, ele não dispara erro

cx.add(82)
cy.add(34)

print(cx.intersection(cy)) # retorna os valores iguais entre os dois
#cx.intersection_update() # já atualiza o cx

cx.isdisjoint(cy) # retorna falso se houver algum elemento igual
cx.issubset(cy) # retorna true se houver algum elemento igual
cx.issuperset(cy) # retorna verdadeiro se todos os elementos de cy está no cx
cx.pop()
cx.remove(82)

print(50 in cx)# retorna true ou false

d = cx.union(cy) # junta os dois conjuntos


