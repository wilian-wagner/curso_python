# Dicionario são compostos por chaves e valores 
# Formato JSON - Javascript Object Notation
# Dicionario não possuem notacao de índice
# Dic = {chave : valor}

dic1 = {'SC':'Santa Catarina','PR':'Paraná','RS':'Rio Grande do Sul'}


# Iterar com for 
for f in dic1.items():
    print(f)

# Iterar com os valores do dicionario
for f in dic1.values():
    print(f)

# Iterar com as chaves do dicionario
for f in dic1.keys():
    print(f)

# Printar os pares sem "{}"
for v,k in dic1.items():
    print(v,k)

# Print comprimento
print(len(dic1))
