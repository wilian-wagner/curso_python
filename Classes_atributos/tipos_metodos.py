# @classmethod - metodo de classe
# @staticmethod - metodos estaticos
# Privete Method - é um método privado __ 2 underline

import random

class Livro():
    ano_atual = 2020
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo   
        self.autor = autor 
        self.ano =ano

    def imprime(self):
        print("Esse livro é %s e o Autor %s" %(self.titulo,self.autor))
    def anopublicacao(self):
        print(" Tempo de Publicação",self.ano_atual - self.ano, "anos")

    @classmethod
    def calculoanopublicacao(vclasse,nome,ano):
        calculo = vclasse.ano_atual - ano   
        return(nome,"Tempo Publicacao", str(calculo), "anos")

    @staticmethod
    def geraisbn():
        isbn = random.randint(0,10000) 
        return isbn

livro1 = Livro("Calculando com Javascipt","ECMA",2019)

livro1.imprime()
livro1.anopublicacao()

livro3 = Livro.calculoanopublicacao("Criando Ondas",1984) 
print(livro3)

print(livro1.geraisbn())