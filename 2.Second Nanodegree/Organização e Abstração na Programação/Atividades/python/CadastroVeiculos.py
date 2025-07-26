import os
from Moto import Moto
from Carro import Carro
from Caminhao import Caminhao

def cadastrar():
    tipo = input("Qual o tipo de veículo: (1) Carro, (2) Moto, (3) Caminhão ")
    if tipo != "1" and tipo != "2" and tipo != "3":
        os.system("cls")
        print("Tipo inválido, reiniciando...")
        return

    os.system("cls")    
    modelo = input("Qual o nome do veículo? ")
    marca = input("Qual a marca? ")
    placa = input("Qual é a placa? ")
    ano = input("Qual é o ano? ")
    if tipo == "1":
        numeroPortas = input("Quantas Portas? ")
        veiculoAdd = Carro(marca, modelo, placa, ano, numeroPortas)
    elif tipo == "2":
        cilindradas = input("Quantas cilindradas? ")
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
    elif tipo == "3":
        capacidade = input("Qual a capacidade do caminhão? ")
        veiculoAdd = Caminhao(marca, modelo, placa, ano, capacidade)
    # adicionando a instancia na lista
    listaVeiculos.append(veiculoAdd)
    os.system("cls")

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
# uma lista que pode ter varios tipos (moto, carro, caminhao)
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