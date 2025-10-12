import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

# FUNÇÃO JOGO   
def jogo():
    
    while(True):
        # Clock
        clock.tick(fps)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Atualizacao


        # Renderizacao

        janela.fill("white")
        pygame.display.flip()

jogo()