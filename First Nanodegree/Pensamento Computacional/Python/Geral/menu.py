import os

while True:
    os.system("cls")
    print("(O) para sair")
    print("(1) para jogo")
    print("(2) para cadastro")
    print("(3) para bônus")
    opcao = input("")
    
    if opcao == "0":
        break
    elif opcao == "1":
        # cai e não faz nada (usar para não deixa vazio)
        pass
    elif opcao == "2":  
        pass
    elif opcao == "3":
        pass
    else:
        print("Opção Inválida")

