from No import No

class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.proximo = nodo
            nodo.anterior = self.fim
            self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("---------------")
        print("Lista Encadeada por ordem de chegada")
        if self.inicio is None:
            print("A lista está vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.proximo
        print("---------------")

    def imprimirReverso(self):
        print("---------------")
        print("Lista Encadeada por ordem de chegada")
        if self.inicio is None:
            print("A lista está vazia!")
        else:
            aux = self.fim
            while aux:
                print( aux.dado )
                aux = aux.anterior
        print("---------------")