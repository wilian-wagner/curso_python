#essa é uma classe filha da super classe Revendedora
from classe_revendedora_superClasse import Revendedora

class RevendedoraCarros(Revendedora):
    def __init__(self):
        super().__init__()
        print("Carro cadastrado")

    def marca(self,marca):
        self.marca = marca
        print("Marca Adcionada")

    def modelo(self,modelo):
        self.modelo = modelo
        print("Modelo Adicionado")


    #Polimofrismo de métodos
    def tipoveiculo(self,tipoveiculo):
        self.tipoveiculo = tipoveiculo
        print("Tipo adicionado para carros")
