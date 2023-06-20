## Objetos iteraveis 
## Podem ser consumidos os valores do seu conteudo
## Basicamente estruturas de dados Lista, Tupla, Dicionario, String

# Iteradores
#  Sao funcoes que consomem e percorrem uma estrutura de dados

# Vamos abrir a caixinha do FOr e entender como ele funciona
# Utilizando os metodos magicos __iter__, __next__
# Métodos m;agicos são funcoes builtins do Python que possuem seus atributos
# São escritos com duplo underline (dunder) __iter__

lista = [1,'carro',54,'Pneu',42,'cabo de vela']

# Primeiro passo do for, checar se é iterável
print(hasattr(lista,'__iter__'))

string = "ABCDEFGHI"
print(hasattr(string,'__iter__'))

# Segundo passo do For, Transformar um iteravel em iterador
nome = "Joao Ricardo"

listaiterador = iter(nome)
print(type(listaiterador))

# Terceiro passo iterar a memoria do objeto com metodo next
print(hasattr(listaiterador,"__next__"))

print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))
print(next(listaiterador))


print("Separador de Nomes")

for a in listaiterador:
    print(a)
    
