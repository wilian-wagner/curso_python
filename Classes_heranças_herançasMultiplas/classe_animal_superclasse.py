 ## Super Classe epara herança multipla 

class Animal():
    def __init__(self,especie):
        self.especie = especie

    def tipo(self):
        return(f" É da especie {self.especie}")
    
    def som(self):
        print(f"A{self.especie} não faz som")
