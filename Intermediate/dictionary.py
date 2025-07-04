UF = {'SP' : 'São Paulo', 'RJ': 'Rio de Janeiro'} #chave-valor, class dict

uf = {}

uf['SP']= 'São Paulo'

D ={}

D['a'] =250
D['a'] = 120
D['b']= 10

x= D['a'] +D['b']

D['a'] += 100

D.clear()

M = {}

M[110] = 48.85
M[9.2] = 'arroz'
M[(1,5,54)] = 45
print(M)
print(M.get(110))

x= M[110]


n1 = {'1' : 1, '2': 2}
n2 = n1.copy() # copia do dicionario em outro local da memoria

print(id(n1))
print(id(n2))

n2 = n1 #mesmo id
print(id(n1))
print(id(n2))

A = {120:'queijo', 134:'arroz', 117:'farinha', 125:'açucar', 133:'macarrao' }
codigos = (111,139,143,157)

A.fromkeys(codigos) #iterar sobre a lista de elementos de acordo com os códigos

#fromkeys, geralmente, é utilizado a partir de um dicionario va
B = {}.fromkeys(codigos,' ') # dicionario criado e todos os elementos terão o valor vazio e a chave de codigos

y= A.pop(117) # recebe e o elemento sai do dicionario
k = A.popitem() #ultimo valor que entrou no dicioonario, sai e retorna como tupla na variavel

u = A.setdefault(150, 'Feijao') #retorna o valor que está lá ou adiciona se não tiver esse elemento(não altera se já existir a chave la)
A.update((180,'Cuzcuz'), (179, 'Farofa'))

print(A.keys()) # retorna todas as chaves
print(A.values()) # retorna todos os valores
print(A.items()) # uma lista de tuplas com os elementos