# Abrir arquivo para leitura sem gerenciador de contexto mais simples

arq1= open('Arquivos/arquivo.txt','r')

# Ler e printar arquivo
print(arq1.read())

# Retornar a primeira linha
arq1.seek(0)
print(arq1.read())


# Fechar arquivo
arq1.close()

# Fazendo gravacao no arquivo e leitura
arq2 = open('Arquivos/arquivo.txt','w+')

## Reescrever arquivo
#arq2.write("Tem nova linha\n")
#arq2.write("Tem nova linha\n")
arq2.seek(0)
print(arq2.read())
arq2.close()

## Alterar o aquivo existente sem apagar o conteudo e leitura
arq3 = open('Arquivos/arquivo.txt','a+')
arq3.write('ALOOOOOOOOOO\n')
arq3.seek(0)
print(arq3.read())


## Manipular arquivos usando gerenciador de contexto de nome
# Nomeando as acoes identando as manipulacoes

with open('arquivos/arquivo.txt','w+') as f:
    f.write("Gerenciador de contexto\n")
    f.seek(0)
    print(f.read())
    f.close()

