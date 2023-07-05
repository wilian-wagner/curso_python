## Quando trabalhamos com herança de classes, por boa prática sempre criamos
# A classe pai ou super classes 'super()''

class Revendedora():
    def __init__(self):
        print("Veiculo Cadastrado")
    
    def tipoveiculo(self,tipoveiculo):
        self.tipoveiculo = tipoveiculo
        print("Tipo adicionado")

    def quantidade(self,quantidade):
        self.quantidade = quantidade
        print("Quantidade adcionada")
    
    def valor(self,valor):
        self.valor = valor
        print("Valor adcionado")
