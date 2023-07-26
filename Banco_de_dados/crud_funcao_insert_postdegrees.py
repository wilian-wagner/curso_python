import psycopg2

conn = psycopg2.connect(host ='db-postgres.postgres.database.azure.com',database = 'db01',user='pgadmin',password ='Jcavi2023')

cursor = conn.cursor()

# cria funçao de insert 

def inserir_registro_input():
    i_nome = input('Nome: ') 
    i_sobrenome = input('Sobrenome: ')
    i_cpf = input('CPF:' )
    cursor.execute("""INSERT INTO cadastro_clientes (nome, sobrenome, cpf) VALUES (%s,%s,%s) """, (i_nome, i_sobrenome, i_cpf))
    conn.commit()
    conn.close()



