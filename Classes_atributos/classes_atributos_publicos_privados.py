## Atributos privados nao sao acessados seus valores pela instancia (encapsulamento)
# Atributos Públicos sao acessíveis pelas instancias sao atributos (abstraidos)

## Atributo Privado e escrito cm 2 underline "__"
#Atributo Protect e escrito com 1 _ (pode ser acessado com uma instancias da sua própria classe
# porem nao acessivel atraves de heranca de classe)
class Cadastro_user():
    def __init__(self,nome,senha):
        self.nome = nome
        self.__senha = senha #atributo encapsulado


#Instanciar 
user1 = Cadastro_user("João",123456)
print(user1.nome)
#print(user1.__senha)

#Função dir lista todos os atributos métodos do objeto 

print(dir(user1))

# Força ler o valor de um atributo privado se chama naming mangling

print(user1._Cadastro_user__senha)

