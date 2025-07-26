from generalFunctions import validaInput, transformaEmAsterisco, limpaTela;
import time, stickman;

'''
Bento Martins - RA 1125095
Pablo Sarturi - RA 1136331
prof pfvr da nota boa pra nós
'''
#region Menu
def menu():
    while True:
        limpaTela()
        print("##### BEM VINDO AO JOGO DA FORCA #####")
        stickman.stickmanAscii(0)
        nomeDesafiante = input("Qual é o nome do Desafiante: ")
        nomeCompetidor = input("Qual é o nome do Competidor: ")
        limpaTela()
        palavra = input("Digite a palavra: ")      
        dicas = registraDicas()
        limpaTela()
        palavraAsteriscos = transformaEmAsterisco(palavra)
        print(f"A palavra tem {len(palavra)} letras: {palavraAsteriscos}\n")
        time.sleep(3)
        menuOpcao = input(
        """Digite (1) para receber uma dica
Digite (2) para jogar
Digite (3) para sair
""")
        if menuOpcao == "1":
            limpaTela()
            jogo(0, palavra, nomeCompetidor, nomeDesafiante, mostraDicas(dicas), dicas, palavraAsteriscos)
        elif menuOpcao == "2":
            limpaTela()
            jogo(0, palavra, nomeCompetidor, nomeDesafiante, True, dicas, palavraAsteriscos)
            # retornar erros
        elif menuOpcao == "3":
            limpaTela()
            print("Que pena! :(")
            quit()
        else:
            limpaTela()
            print("Digite uma opção válida! Reiniciando sistema...")
            time.sleep(2)

def jogarNovamente():
    if input("Digite 's' para jogar novamente: ").lower() == "s":
        menu()
    else:
        print("OK! Você quer sair do jogo então... :(")
        time.sleep(2)
        quit()
#endregion

#region Dicas
def mostraDicas(dicas):
    limpaTela()
    if len(dicas) > 0:
        print(f"A dica é: '{dicas[0]}'")
        del dicas[0]
    else:
        print("Você não tem mais dicas!")
    time.sleep(5)
    limpaTela()
    return len(dicas) == 0

def registraDicas():
    dicas = []
    i = 0
    print("")
    for i in range(3):
        dicas.append(input(f"Insira a dica {i+1}: "))
    return dicas
#endregion

#region Jogo
def inputLetra(podeDica):
    if podeDica:
        return input("Digite a letra (ou escreva 'dica' para receber uma dica): ")
    else:
        print("Depois de receber a dica, você é obrigado a chutar uma letra!")
        return input("Digite a letra: ")

def incrementaErros(contadorErros, palavra, nomeDesafiante, nomeCompetidor):
    contadorErros += 1
    stickman.stickmanAscii(contadorErros)
    if contadorErros >= 5:
        if contadorErros == 5:
            print(f"Última chance! ### Você errou {contadorErros} vez(es) ###")
        else:
            print(f"Você Perdeu! A palavra era: {palavra}")
            time.sleep(5)
            limpaTela()
            print(f"Dessa vez o(a) desafiante {nomeDesafiante} ganhou!")
            print(f"Mas você não vai deixar assim né {nomeCompetidor}...?")
            time.sleep(8)
            limpaTela()
            jogarNovamente()
    else:
        print(f"### Você errou {contadorErros} vez(es) ###")
    return contadorErros

def palavraDescoberta(palavra, nomeDesafiante, nomeCompetidor):
    limpaTela()
    print(f"Parabéns! Você acertou! A palavra era: {palavra}")
    print(f"O(a) competidor(a) {nomeCompetidor} se deu melhor contra o(a) desafiante {nomeDesafiante} dessa vez...")
    print(f"E aí {nomeDesafiante}, vai deixar barato?")
    time.sleep(8)
    limpaTela()
    jogarNovamente()

def jogo(contadorErros, palavra, nomeCompetidor, nomeDesafiante, podeDica, dicas, palavraAsteriscos):
    letrasJaEscolhidas = []
    while contadorErros <= 6:
        limpaTela()
        letraExiste = False
        valido = False
        letraEscolhida = inputLetra(podeDica)
        letraEscolhida = letraEscolhida.lower()
        if letraEscolhida == "dica" and podeDica == True:
            podeDica = mostraDicas(dicas)
        else:
            # caso tenha escrito dica, no momento em que é obrigatorio colocar uma letra, não deve deixar passar
            valido = validaInput(letraEscolhida)
            if not letraEscolhida == "dica":
                podeDica = True
        jaAdivinhada = False
        if valido == True and podeDica == True:
            limpaTela()
            if letraEscolhida not in letrasJaEscolhidas:
                letrasJaEscolhidas.append(letraEscolhida)
            else:
                print(f"A letra '{letraEscolhida}' já foi chutada!")
                jaAdivinhada = True
            for indexNum, letra in enumerate(palavra.lower()):
                if letra == letraEscolhida:
                    letraExiste = True
                    palavraAsteriscos = palavraAsteriscos[:indexNum] + letraEscolhida + palavraAsteriscos[indexNum + 1:]
            if letraExiste and not jaAdivinhada:
                print(f"A letra existe: {palavraAsteriscos}")
            elif not jaAdivinhada:
                print(f"A letra não existe: {palavraAsteriscos}")
                contadorErros = incrementaErros(contadorErros, palavra, nomeDesafiante, nomeCompetidor)
            print(f"\nLetras já ditas: {letrasJaEscolhidas}")
            time.sleep(4)
            if "*" not in palavraAsteriscos:
                palavraDescoberta(palavra, nomeDesafiante, nomeCompetidor)
#endregion

try:
    menu()
except Exception as error:
    print(error)
