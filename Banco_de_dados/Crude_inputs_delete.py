import sqlite3
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()
#Passando as informações de Input
u_id = input("Insira o Id de Cadastro Para Excluir: ")
cursor.execute("""
delete from cadastro_clientes WHERE id = ?
""", (u_id,))
conn.commit()
cursor.execute(""" select * from cadastro_clientes """)
for reg in cursor.fetchall(): print (reg)
#Fechando conexão com Banco de dados 
conn.close()