import sqlite3

#abrir definição de conexão 
conn = sqlite3.connect('cadastro.db')

# Iniciar cursor
cursor = conn.cursor()

# Executar açào sql
cursor.execute("""
INSERT INTO cadastro_clientes (nome,sobrenome,cpf) VALUES ('João', 'Cavichiolli','7773554444') """)
cursor.execute("""
INSERT INTO cadastro_clientes (nome,sobrenome,cpf) VALUES ('Valéria', 'Cunha','553333') """)

# comita na base de dados
conn.commit()

cursor.execute("select * from cadastro_clientes")

for regs in cursor.fetchall():
    print (regs)

conn.close()
