import os
os.system("cls")
print("######################")
print("Responda com S ou N")
print("######################")

telefonou = input("Telefonou para a vítima? ")
esteve = input("Esteve no Local? ")
mora = input("Mora perto da vítima? ")
devia = input("Devia para a vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")

colecaoPerguntas = [telefonou, esteve, mora, devia, trabalhou]
contadorSim = 0
for pergunta in colecaoPerguntas:
    if pergunta == "s" or pergunta == "S":
        contadorSim += 1

print("#################")
if contadorSim < 2:
   print("Você é inocente!")
elif contadorSim == 2:
    print("Você é um suspeito!")
elif contadorSim <= 4:
    print("Você é cúmplice")
else:
    print("Você é o assaltante!")
print("#################")
