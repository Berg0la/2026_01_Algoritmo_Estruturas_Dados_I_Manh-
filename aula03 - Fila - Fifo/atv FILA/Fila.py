from Moto import Moto

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, bike):
        if self.inicio is None:
            self.inicio = bike
            
        else:
            self.fim.prox = bike
        self.fim = bike

    def imprimir(self):
        print("-" * 10)
        if self.inicio is None:
            print("Fila de Motos Vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux)
                aux = aux.prox

    def lavar(self):
        if self.inicio is None:
            print("Não há motos para lavar")
        else:
            print("Carro lavado: ")
            print(self.inicio)
            aux = self.inicio
            self.inicio = self.inicio.prox
            del(aux)
            if self.inicio is None:
                self.fim = None
