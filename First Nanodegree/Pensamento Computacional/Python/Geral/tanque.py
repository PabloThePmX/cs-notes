import os
os.system("cls")

tanque = 1000
while tanque > 0:
    abastecido = int(input("Litros abastecidos: "))
    if abastecido > tanque:
        print("Não temos essa quantidade disponível")
    else:
        tanque -= abastecido
        print(f"Restam {tanque} litros")
print("\nAcabou a gasolina!!")