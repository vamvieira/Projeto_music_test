class Instrumento:
    def tocar(self):
        print("Tocando")

    def limpar(self):
        print("Limpando")

    def destruir(self):
        print("Destruindo")

class Violino(Instrumento):
    def __init__(self):
        self.cordas = 4
        self.material = "aço"

    def get_cordas(self):
        self.cordas = 5
        print(self.cordas)

    def tocar(self):
        print("Som do Violino")

    def limpar(self):
        print("Limpando o Violino")

violino = Violino()
violino.tocar()
violino.limpar()
print(violino.cordas)


violino.get_cordas()
print(violino.cordas)
print(violino.material)

instrumento = Instrumento()
print(instrumento.tocar())

class Clarinete(Instrumento):
    def tocar(self):
        print("Som do Clarinete")

    def limpar(self):
        print("Limpando o Clarinete")

    def destruir(self):
        print("Quebrando o Clarinete")