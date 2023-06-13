## Junta as estruturas de dados e retona uma tupla 

dic_frutas = {1:"Maca",2:"Laranja",3:"Maca"}

dic_verdura = {1:"Cebola",2:"Beterraba",3:"Alface",4:"Repolho"}

junta = (list(zip(dic_frutas,dic_verdura)))
print(junta)

print(list(zip(dic_frutas.values(),dic_verdura.values())))



