import psycopg2

conn = psycopg2.connect(host ='db-postgres.postgres.database.azure.com',database = 'db01',user='pgadmin',password ='Jcavi2023')

cursor = conn.cursor()

# cria funçao de insert 

def atualizar_tabela():
    u_id = input("Insira o Id de Cadastro: ")
    u_nome = input(' Insira o Novo Nome: ')
    u_cpf = input(' Insira o Novo CPF: ')
    cursor.execute("""UPDATE cadastro_clientes SET nome = %s, cpf = %s WHERE id = %s""", (u_nome, u_cpf, u_id))     
    conn.commit()
    conn.close()

