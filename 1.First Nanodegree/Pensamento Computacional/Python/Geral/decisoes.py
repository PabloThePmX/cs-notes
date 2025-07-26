nome = input("Nome: ")
idade = int(input("Idade:"))
if idade >= 18:
    #colocar o f na frente para ter interpolação
    print(f"O {nome} pode entrar!")
else:
    print("Banido")