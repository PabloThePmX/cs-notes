import os
from Veiculo import Veiculo

def cadastrar():
    modelo = input("Qual o nome do carro? ")
    marca = input("Qual a marca? ")
    placa = input("Qual é a placa? ")
    ano = input("Qual é o ano? ")
    listaVeiculos.append(Veiculo(marca, modelo, placa, ano))

def listar():
    if len(listaVeiculos) > 0:
        for veiculo in listaVeiculos:
            print(f"Veículo {listaVeiculos.index(veiculo) + 1}: {veiculo}")
    else:
        print("Não existem veículos cadastrados.")

def excluir():
    placa = input("Digite a placa do carro que deseja excluir: ")
    encotrou = False
    for veiculo in listaVeiculos:
        if placa == veiculo.get_placa():
            listaVeiculos.remove(veiculo)
            encotrou = True
            break
    if not encotrou:
        print("Placa não encontrada.")


os.system("cls")
listaVeiculos = []
while True:
    
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluír Veículo")
    print("0 - SAIR")
    try:
        opcao = int(input())

        # cadastro
        if opcao == 1:      
            os.system("cls")
            cadastrar()
        # listar
        elif opcao == 2:
            os.system("cls")
            listar()
        # excluir
        elif opcao == 3:
            os.system("cls")
            excluir()
        # sair
        elif opcao == 0:
            break
    except:
        print("Char inválido!")