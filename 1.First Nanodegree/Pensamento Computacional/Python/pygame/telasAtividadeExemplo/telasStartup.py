import pygame

def inicio(): 
    pygame.init()
    tamanho = (800, 600) # tupla
    # indicando o tamanho da tela
    tela = pygame.display.set_mode(tamanho)
    # nome que aparece na janela
    pygame.display.set_caption("exemplo 1")
    return tela