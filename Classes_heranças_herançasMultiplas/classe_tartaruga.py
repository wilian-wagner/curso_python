#recebe jheranca multipla

from classe_animal_marinho import Aquatico
from classe_animal_terrestre import Terrestre

class Tartaurga(Aquatico,Terrestre):
    def __init__(self, especie):
        super().__init__(especie)

t1 = Tartaurga("Marinha")
t1.tipo()
t1.som()

t2 = Tartaurga("Jabuti")
t2.tipo()
t2.som()