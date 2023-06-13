# Reduz o valor dos iteraveis a um unico valor

from functools import reduce
lista = [2,3,4]

def mult (x,y):
    return x*y

print(reduce(mult,lista))

# Teste para ver o maior valor da lista (max)
lista2 = [120,88,104,1,400]
testemaior = lambda x,y: x if(x>y) else y 
print(reduce(testemaior,lista2))

