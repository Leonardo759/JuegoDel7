import random

class Dado:

    def __init__(self):
        self.valor=0

    def tirarDado(self):
        sef.valor=random.randint(1, 6)

    def getValor(self):
        return self.valor
