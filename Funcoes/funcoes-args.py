
## Funcoes args retornam tuplas
def numeros(*args):
    print(args)

# Chamar a Funcao com Args
numeros(3,5,1,2,78,190,22)

# Input via cmd 
# nome = input("Digite o seu nome:")

def soma_total(*args):
    total = 0 
    for numero in args:
        total= total +numero
    return total

print(soma_total(4,6,1,73,12,90))
