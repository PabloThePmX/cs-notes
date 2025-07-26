import pygame

pygame.init()
tamanho = (800, 600) # tupla
# indicando o tamanho da tela
tela = pygame.display.set_mode(tamanho)
# nome que aparece na janela
pygame.display.set_caption("exemplo 1")
# define a cor da tela

corBranca = (255,255,255) # RGB
corPreta = (0,0,0)
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(corBranca)

    pygame.draw.line(tela, corPreta, (50, 50), (750, 50))
    pygame.draw.line(tela, corPreta, (50, 50), (375, 550))
    pygame.draw.line(tela, corPreta, (750, 50), (375, 550))

    pygame.display.update()

    clock.tick(60)