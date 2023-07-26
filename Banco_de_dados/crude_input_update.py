import sqlite3
conn = sqlite3.connect('cadastro.db') 
cursor = conn.cursor()
#Passando as informações de Input
u_id = input("Insira o Id de Cadastro: ") 
u_nome = input(' Insira o Novo Nome: ')
u_cpf = input(' Insira o Novo CPF: ')
cursor.execute("""
UPDATE cadastro_clientes SET nome = ?, cpf = ? WHERE id = ?
""", (u_nome, u_cpf, u_id))
conn.commit()
#Executando a Leitura da Alteração com o Select
cursor.execute(""" select * from cadastro_clientes where id = ? """,(u_id,))
for reg in cursor.fetchall(): print (reg)
#Encerrando a Conexão com Banco de dados conn.close()