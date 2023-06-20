## Para manipular arquivos csv temos que importar o modulo csv

import csv

with open('arquivos/nomes.csv','w', newline="") as fcsv:
    escrever = csv.writer(fcsv,delimiter=',')
    escrever.writerow(("Nome","Sobrenome","Idade"))
    escrever.writerow(("Joao","Ricardo","35"))
    escrever.writerow(("Juca","Souza","23"))
    escrever.writerow(("Alberto","Cunha","54"))

with open('arquivos/nomes.csv','r') as fcsv2:
    ler = csv.reader(fcsv2)
    l1 = list(ler)
    print(l1)
#    for i in l1:
#        print(i)

with open('arquivos/arquivo1.csv','r') as fcsv3:
    ler = csv.reader(fcsv3)
    l2 = list(ler)
#    for i in l2:
#        print(i)

with open('arquivos/arquivo1.csv','r') as fcsv4:
    ler_dict = csv.DictReader(fcsv4)

#    for dic in ler_dict:
#        print(dic)

    for dic in ler_dict:
        print(dic['SaleNumber'])