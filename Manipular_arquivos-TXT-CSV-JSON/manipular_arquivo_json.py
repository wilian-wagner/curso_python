## Para Trabalhar com JSON utilizar o modulo JSON

import json

import urllib.request
# Criar um dicionario com uma informacao de json

cadastro_pessoas = {
    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}
# Iterar dicionario

for c,v in cadastro_pessoas.items():
    print(c,v)

# Transforma em formato JSON com json.dumps
dados = json.dumps(cadastro_pessoas,indent=4)
print(dados)

with open('arquivos/pessoas.json','w+') as j:
# json.dump = write
    json.dump(cadastro_pessoas,j,indent=4)

# Ler o arquivo criado
#with open('arquivos/pessoas.json','w+') as f:
#json.load = read
    #le_json = json.load(f)

#    for v in le_json.values():
#        print(v)


# Capturar dados de url em formato Json
url = "http://api.open-notify.org/astros.json"
pega_json =urllib.request.urlopen(url).read().decode()

#Converter em dicionario

dic_json = json.loads(pega_json)
for c in dic_json.values():
    print(c)

print(dic_json)
# FIltrando pela chave people iterou pela chave name

for c in dic_json['people']:
    print(c['name'])

