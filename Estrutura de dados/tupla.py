# A tupla é muito parecida com a lista
# São imutaveis, não é possível add ou remover elementos 
# Tupla são mais perfomaticas (devido a sua imutabilidade)

t1 = "João", "Pedro"
t2 = ("João", "Pedro")
t3 = 'João'
t4 = "João",

print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

# A tupla e definida pela virgula
# Excetos ela estiver  dentro de outra estrutura de dados

t5 = [(45,60),]
print(t5)

t6 = 1,6,8,10
for t in t6: 
    print(t)

# Refatorar(reescrever) a tupla
t6 = 1,6,8,10,20
print(t6)
