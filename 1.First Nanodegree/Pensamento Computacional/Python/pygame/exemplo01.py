import pygame

pygame.init()

# define a taxa de atualização por segundo (FPS?)
clock = pygame.time.Clock()
tamanho = (800, 600) # tupla
# indicando o tamanho da tela
tela = pygame.display.set_mode(tamanho)
# nome que aparece na janela
pygame.display.set_caption("exemplo 1")

# define a cor da tela
corBranca = (255,255,255) # RGB
corPreta = (0,0,0)

moveBolinha = 400

while True: 
    for evento in pygame.event.get():
        # a função do quit é maiúscula
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(corBranca)

    pygame.draw.circle(tela, corPreta, (moveBolinha, 300), 30)
    pygame.draw.line(tela, corPreta, (0, 250), (800, 250), 3)
    pygame.draw.line(tela, corPreta, (0, 350), (800, 350), 3)
    pygame.draw.rect(tela, corPreta, (400,300, 60, 60), 3)
    #  atualiza a tela com o que foi definido
    pygame.display.update()
    moveBolinha = moveBolinha + 1

    clock.tick(60)


pygame.quit()

