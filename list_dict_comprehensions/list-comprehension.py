## List comprehension é uma forma otimizada de 
## criar estruturas de dados em forma de lista
## aplicando uma acão de manipulacão resultando em lista

# lista comum
listanumeros = [1,5,21,78,12,80]

# list comprehension basta digitar em formato de lista

#list comprehension 
lc1 = [multiplica * 2 for multiplica in listanumeros]
print(lc1)

listapares = [p for p in range(20) if p % 2 == 0]
print(listapares)

listanomes = ["Joao","alberto", "juca", "afonso"]

lc2 = [troca.replace('a','@') for troca in listanomes]
print(lc2)