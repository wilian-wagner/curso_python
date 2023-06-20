## Funcoes em objetos geradores possuem maior performace de memória
## Pois não carregam todos os elementos para memória antes de executar 
## Executam e descarregam no mesmo momento


import time
import sys

def funcgerador():
    l = []
    for n in range(100):
        l.append(n)
        time.sleep(0.1)
    return l

#gen = funcgerador()

#Mostrar tipo da funcao 
print(type(funcgerador))

# Iterar a lista de numeros criada
#for i in gen:
#   print(i)

## Utilizar uma funcao Geradora. Uma funcao ela utiliza um recurso chamado yield

def funcgerador2():
    for n in range(100):
        yield n
        time.sleep(0.1)

# Atribuir a funcao a uma variavel

gen2 = funcgerador2()

# Mostar o tipo da funcao

print(type(gen2))

#for i in gen2:
#    print(i)


## Transformar uma list comprehension em gerador e ver o tamanho e uso de memoria
lc1 = [i for i in range(10000)]

#for i in lc1:
#   print(i)

## Transformar em gerador

gen1 = (i for i in range(1000000000000000000000000000000000000000000000000000))

print(type(lc1))
print(type(gen1))

print(sys.getsizeof(lc1))
print(sys.getsizeof(gen1))

