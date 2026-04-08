from Moto import Moto
from Fila import Fila

fila = Fila()

op =+ -1
while op is not 0:
    print("1) Adicionar moto")
    print("2) Imprimir fila")
    print("3) Lavar moto")
    print("0) Sair")

    op = int(input("Digite sua opção: "))
    

    if op == 1:
        moto = Moto()
        moto.modelo = input("Modelo: ")
        moto.placa = input("Placa: ")
        moto.ano = int(input("Ano: "))
        fila.add(moto)
    if op == 2:
        fila.imprimir()

    if op == 3:
        fila.lavar()

    if op == 0:
        print("Saída com sucesso.")
        break

    if op > 3 or op < 0:
        print("Opção invalida!") 
