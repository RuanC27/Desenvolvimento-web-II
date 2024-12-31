class Problema:
    def __init__(self, variavel1, variavel2):
        self.variavel1 = int(variavel1)
        self.variavel2 = int(variavel2)

    def calcular(self):
        return self.variavel1 + self.variavel2
