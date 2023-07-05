# Getters e Setters é um conceito de boas práticas de abstração e encapsulamento em POO

#Getter transforma um atributo privado em um método publico
#Setter transforma a ação de um método existente aplicando uma modificação sem alterar
#Os métodos existentes para um objeto que foi instanciado

class Vendaprodutos():
    def __init__(self,produto,quantidade,valor):
        self.__produto = produto 
        self.__quantidade = quantidade 
        self.__valor = valor

        ## Abstração com getters 
    @property
    def produto(self):
        return self.__produto
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade            


produto1 = Vendaprodutos("Arroz",34,12.45)
produto2 = Vendaprodutos("Feijão",10,8.5)

print(produto1.produto) 
print(produto2.quantidade)

produto2.quantidade = 20

print(produto2.quantidade)



