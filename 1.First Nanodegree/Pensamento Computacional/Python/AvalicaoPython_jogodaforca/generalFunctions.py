import os, time, platform

# auxiliares
def validaInput(letraEscolhida):
    valido = False
    if len(letraEscolhida) == 1:
        valido = True
    else:
        print("Digite apenas uma letra!")
        time.sleep(3)
        os.system("cls")
    return valido

def transformaEmAsterisco(palavra):
    palavraAsteriscos = len(palavra) * "*"
    return palavraAsteriscos

def limpaTela():
    # https://stackoverflow.com/a/10091465
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
