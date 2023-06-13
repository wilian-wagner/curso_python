import math

# Aplica uma acão pré determinada para cadsa elemento no momento da execucão
#Resultando a acão final

numeros = [12,6,67,19,20]

def soma (x):
    return x+2

# Executar map
print(list(map(soma,numeros)))

# Raiz quadrada dos valores da lista

print(list(map(math.sqrt,numeros)))

