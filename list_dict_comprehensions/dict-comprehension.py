## Forma de escrever e manipilar um dicionario de forma otimizada 

listadict = [
    ('valor1',10),
    ('valor2',8),
    ('valor3',30),
]

d1 = { c:v for c,v in listadict}
print(d1)

d2 = { c:v*2 for c,v in listadict}
print(d2)
