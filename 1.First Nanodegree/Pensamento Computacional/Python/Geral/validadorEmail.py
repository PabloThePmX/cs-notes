temArroba = False
temPonto = False
email = input("Insira o seu email: ")
# como string é coleção, podemos ler ela
for letra in email:
    if letra == "@":
        temArroba = True
    elif letra == ".":
        temPonto = True

if temArroba == True and temPonto == True:
    print("E-mail válido.")
else:
    print("E-mail inválido.")
