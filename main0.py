import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

img_personagens = pygame.image.load("imagem/personagem/amigo/0.png").convert_alpha()


# FUNÇÃO JOGO   
def jogo():

    x_pos = 100
    y_pos = 300
    x_vel = 0
    y_vel = 0
    vel = 5
    
    while(True):
        # Clock
        clock.tick(fps)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_vel = vel
                if event.key == pygame.K_LEFT:
                    x_vel = -vel
                if event.key == pygame.K_UP:
                    y_vel = -vel
                if event.key == pygame.K_DOWN:
                    y_vel = vel

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_vel = 0
                if event.key == pygame.K_LEFT:
                    x_vel = 0
                if event.key == pygame.K_UP:
                    y_vel = 0
                if event.key == pygame.K_DOWN:
                    y_vel = 0

        # Atualizacao
        
        x_pos += x_vel
        y_pos += y_vel

        # Renderizacao

        janela.fill("white")
        janela.blit(img_personagens, (x_pos, y_pos))
        pygame.display.flip()

jogo()