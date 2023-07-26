import sqlite3

# Criar a string de conexão 

conn = sqlite3.connect('cadastro.db')

# Abrir cursor

cursor = conn.cursor()

cursor.execute( """
create table cadastro_clientes (
id integer NOT NULL PRIMARY KEY AUTOINCREMENT, nome varchar(100) not null,
sobrenome varchar(100) not null,
cpf varchar(11) not null
);
""" )
# Fechat conexao

conn.close()

##Comando DDL são definições de estrututura 
# Create Alter Drop
##Cm