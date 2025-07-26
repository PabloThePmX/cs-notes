import os
os.system("cls")
valorGolpes = []
pomekons = []
i = 0

while valorGolpes.__len__() < 2:
    pomekons.append(input("\nInsira o nome do seu POMEKON: "))

    levelTreinador = int(input(f"Defina o level do treinador do {pomekons[i]}: "))
    ataquePomekon = int(input(f"Defina o atk do {pomekons[i]}: "))
    defesaPomekon = int(input(f"Agora defina a defesa do {pomekons[i]}: "))

    if levelTreinador % 2 == 0:
        bonusPomekon = int(input(f"Informe o bonus do {pomekons[i]}: "))
    else:
        bonusPomekon = 0

    valorGolpes.append(((ataquePomekon + defesaPomekon)/2) + bonusPomekon)

    i += 1

print("")
if valorGolpes[0] > valorGolpes[1]:
    print(f"O vencedor do duelo foi {pomekons[0]} pois {valorGolpes[0]} > {valorGolpes[1]}")
else:
    print(f"O vencedor do duelo foi {pomekons[1]} pois {valorGolpes[1]} > {valorGolpes[0]}")