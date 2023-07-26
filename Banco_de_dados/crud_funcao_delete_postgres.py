import psycopg2

conn = psycopg2.connect(host ='db-postgres.postgres.database.azure.com',database = 'db01',user='pgadmin',password ='Jcavi2023')

cursor = conn.cursor()

# cria funçao de insert 

def deleta_dados():
    u_id = input("Insira o Id de Cadastro Para Excluir: ")
    cursor.execute(' delete from cadastro_clientes WHERE id = %s',(u_id,))
    conn.commit()
    conn.close()


