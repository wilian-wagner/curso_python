import psycopg2

conn = psycopg2.connect(host ='db-postgres.postgres.database.azure.com',database = 'db01',user='pgadmin',password ='Jcavi2023')

cursor = conn.cursor()

# cria funçao de insert 

def leitura_da_tabela():
    cursor.execute("select * from cadastro_clientes")
    for reg in cursor.fetchall():
        print(reg)
    conn.commit()
    conn.close()


