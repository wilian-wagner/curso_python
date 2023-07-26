from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(250), nullable=False)
    sobrenome = Column(String(250), nullable=False)
    cpf = Column(String(250), nullable=False)
# MySQL
#engine = create_engine('mysql+pymysql://python:python123@localhost/banco01')
# Postgres
engine = create_engine('postgresql+psycopg2://pgadmin:Jcavi2023@db-postgres.postgres.database.azure.com/db01')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create
novo_cliente = Clientes(nome='AAAAAA', sobrenome='BBBBB',cpf='12345678909')
session.add(novo_cliente)
session.commit()

# Read
select_clientes = session.query(Clientes).all()
for regs in select_clientes:
    print(regs.id, regs.nome, regs.sobrenome,regs.cpf)

# Update
update_clientes = session.query(Clientes).filter_by(id=3).first()
update_clientes.nome = 'Marina'
session.commit()

# Delete
delete_clientes = session.query(Clientes).filter_by(id=9).first()
session.delete(delete_clientes)
session.commit()

session.close()