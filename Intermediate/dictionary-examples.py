cores = {1 :'azul', 2:'verde', 3:'vermelho'}

for x in cores.keys(): #keys é default, nao precisa colocar
    print(f' {x} - {cores[x]}')

for x in cores.values():
    print(f' {x}')
print('fim')

#iteração conjunta chave-valor

for x in cores.items():
    print(f' {x[0]} - {x[1]}') #indice 0 é o numero, e o 1, nome da cor

for numero,cor in cores.items():
        print(f' {numero} - {cor}')  # indice 0 é o numero, e o 1, nome da cor