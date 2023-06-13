## Lista é uma estrutura de dados fininta 
# Lista Homogenea
l1 = ["Ferrari", "Red Bull", "Mercedes", "Aston Martin"]

# Printar lista homogenea
print(l1)
print('______________________')
# Trazer dados de um enedereco de memória 
print(l1[3])
print('______________________')
# iterar uma estrutura de dados
for l in l1:
    print(l) 
print('______________________')

# Ordenar em ordem crescente 
l1.sort()
print(l1)
print('______________________')

# Orde a lista em ordem diferente
l1.reverse()
print(l1)
print('______________________')

# Lista heterogenea
l2 = [2022,'João',67.34,'Pedro']
#l2.sort() nao é possvel ordenar listas heterogeneas

# Adcionar um intem a lista 
l1.append("Ãlpine")
print(l1)
print('______________________')

# Adcionar mais de um item a lista
l1.extend(['Alpha Tauri','Williams'])
print(l1)
print('______________________')

# remover um item especifico da lista
l1.remove("Ferrari")
print(l1)
print('______________________')

# Duck typing = Estruturas parecidas utilizam-se das mesmas funcionalidades
# Recusos e manipulacoes dentro da linguagem 