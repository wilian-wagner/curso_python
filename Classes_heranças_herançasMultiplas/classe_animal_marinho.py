# Classe filha da classe animal 

from classe_animal_superclasse import Animal
class Aquatico(Animal):
    def __init__(self, especie):
        super().__init__(especie)
        
    def tipo(self):
        return print(f"é da especie {self.especie} que nada no mar")
