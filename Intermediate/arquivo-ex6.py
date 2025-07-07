#codificação arquivos

codGravacao = input('Digite a codificação de gravação: ')#ANSI E UTF-8
codLeitura = input('Digite a codificação de leitura: ')

print('Etapa de gravação de arquivo')
arq = open('codificacao.txt','w', encoding=codGravacao )
arq.write('Gravação de arquivo\n')
arq.write('acentos: á, é, í, Á, É, Í, ç, Ç\n')
arq.close()

print('\nEtapa de leitura do arquivo')
arq = open('codificacao.txt','r', encoding=codLeitura)
s = arq.readline()
print(s.rstrip())
s= arq.readline()
print(s.rstrip())
arq.close()

print('Fim')