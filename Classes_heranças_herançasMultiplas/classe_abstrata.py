# Classes abstratas são classes criadas para serem modeos ou template para outras classes
# Classe utilizada como SuperClasse ou parar ser herdada em classes filhas

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,tipo,especie):
        self.tipo = tipo
        self.especie = especie
    
    @abstractmethod
    def raca(self):
        pass