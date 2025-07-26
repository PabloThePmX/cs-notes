import os

def cocos_macaco():
    passou = False
    cocosMacaco = int(input("\nQuantos cocos o macaco tem? "))
    print("\nAgora me diga quantos cocos o macaco tem, se eu pegar metade dos cocos que ele tem, mais dois cocos, e depois subtrair três cocos?")
    cocosUsuario = int(input("\nQual é a sua resposta? "))
    cocosMacacoResult = (cocosMacaco/2)+2-3
    if cocosMacacoResult == cocosUsuario:
        passou = True
        print(f"-> CORRETO! O macaco tem {cocosMacacoResult} cocos! <-")
    return passou

def labirinto_crocodilo():
    passou = False
    respostaUsuario = int(input("""\nSe eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura,
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com
segurança? """))
    if respostaUsuario == (12-7):
        passou = True 
        print(f"-> CORRETO! Você tem {12-7}m para amarrar nas árvores! <-")
    return passou

def enigma_final():
    numeroTesourosUsuario = int(input("""\nSe o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras,
e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número
total de periquitos é 42, quantos tesouros tem na ilha? """))
    numeroTesouros = (42*3)*2
    if numeroTesourosUsuario == numeroTesouros:
        passou = True
        print(f"-> CORRETO! A ilha tem {numeroTesouros} tesouros! <-")
    return passou

def game_over():
    print("--------> GAME OVER <--------")
    quit()
    
os.system("cls")
# colocar três """ para string com caracteres especias, espaços e afins
print("""Você é um explorador corajoso em busca de tesouros lendários na
misteriosa Ilha Maluca. Rumores dizem que um grande tesouro está
escondido em algum lugar na ilha, mas para encontrá-lo, você
precisa decifrar uma série de enigmas.
      
Ao chegar na ilha, você se depara com uma placa estranha com
inscrições antigas. As inscrições dizem o seguinte:
"Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os
desafios a seguir e siga as instruções para encontrar o caminho certo."

Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
pela porta e continuar sua jornada, você precisa responder a seguinte questão:""")
passou = cocos_macaco()
if passou == False:
    game_over()

print("""\nApós passar pela porta, você entra em um labirinto infestado de
crocodilos famintos. Para escapar deles, você precisa resolver o seguinte
problema:""")
passou = labirinto_crocodilo()
if passou == False:
    game_over()

print("""\nFinalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um
enigma final:""")
passou = enigma_final()
if passou == False:
    game_over()

print("\nPARABÉNS!!!! Você é um verdadeiro explorador!")


