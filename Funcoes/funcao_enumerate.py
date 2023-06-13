## Funcao enumerate, enumera os indices de uma estrutura de dados

li = ["Florianopolis", "Biguacu","Palhoca", 'São José']

print (list(enumerate(li)))

# Iterar com enumerate 
for l,i in enumerate(li):
    print(l,i)

# Iterador com condicional dos indices 
for i, valor in enumerate(li):
    if i >1:
        break
    else:
        print(valor)



