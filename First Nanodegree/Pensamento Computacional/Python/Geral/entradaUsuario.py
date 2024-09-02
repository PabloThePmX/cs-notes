## todos os valores de input sao em string, por isso precisa converter
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1+nota2)/2
print("A nota final é:", media)

if media >= 7:
    print("Você passou!")
elif media >= 3:
    print("Você ficou em exame!")
else:
    print("Foi mal, você reprovou!")
    