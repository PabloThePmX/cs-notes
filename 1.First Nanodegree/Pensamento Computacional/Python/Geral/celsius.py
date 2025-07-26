celsius = float(input("Informe a temperatura em celsius: "))
fah = celsius * (9/5) + 32
print("O valor convertido em Fº", fah)
## o {} diz que vai ser injetado um trecho de código no meio da string
## usa .format pq ele é filho da string (e nesse caso, ele está sendo executado dentro da string)
print("{:.3f} Cº convertido em Fº: {:.3f}" .format(celsius, fah))