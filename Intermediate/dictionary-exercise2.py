'''ler dados dos estados brasileiros : sigla, nome, capital e pis.
a sigla deve ser usado como chave para o dicionario e o valor de ser um dicionario aninhado contendo
os objetos Nome, Capital, PIB. Uma string vazia para a sigla termina a inserção. Exibir dados na tela'''



UF = {}

while True:
        sigla = input( ' Digite a sigla: ')
        if sigla =='':
            break
        elif sigla in UF:
            print(f'a sigla {sigla} já está no cadastro.')
            continue
        estado = input('Digite o nome do estado: ')
        capital = input('Digite a capital: ')
        pib = float(input('Digite o PIB: '))
        item = {'nome': estado, 'capital': capital, 'pib' : pib}
        UF[sigla] = item


print(' {:15} {:15} {:>10}' .format('Estado','Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
    print('({}) {:20} {:15} {:10.1f}' .format(
        sigla,
        dados['nome'],
        dados['capital'],
        dados['pib']
    ))