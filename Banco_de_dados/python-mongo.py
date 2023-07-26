# importando o Modulo
from pymongo import MongoClient

#Conectando ao MongoDB
conn = MongoClient('172.16.91.51', 27017)

# Conectando ao banco de dados
db = conn.ecommerce


# Criando uma Collection na Base de Dados Chamada Produtos.
col_produtos = db.produtos

prod1 =   {  "_id": 22,
                "Nome": "Marreta de desempenar vidro",
                "Fabricante": "Makita",
                "valor": 666,
                "estoque": 10
}

prod2 =   {  "_id": 29,
                "Nome": "Esquadro redondo",
                "Fabricante": "Pitágoras",
                "valor": 345,
                "estoque": 22
}

#Inserindo os dados na collection

col_produtos.insert_one(prod1)

# Testando se inseriu com comando FindOne

print(col_produtos.find_one({}))

# Adicionando Segundo Produto

col_produtos.insert_one(prod2)

# Criando um cursor para repetir as operações de consulta e executando 
# com laço for

for doc in col_produtos.find():
    print(doc)