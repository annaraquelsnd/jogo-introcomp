import pygame
import botao as bt

pygame.init()

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

img_fundo = pygame.image.load("imagem/fundo/selecao_fundo.webp").convert_alpha()
img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

img_quadro = pygame.image.load("imagem/fundo/quadro.png").convert_alpha()
img_cursor = pygame.image.load("imagem/fundo/cursor.png").convert_alpha()


bt_personagem1 = bt.Botao(img_quadro, 150, 135, 1, img_cursor)
bt_personagem2 = bt.Botao(img_quadro, 360, 135, 2, img_cursor)
bt_personagem3 = bt.Botao(img_quadro, 150, 385, 3, img_cursor)
bt_personagem4 = bt.Botao(img_quadro, 360, 385, 4, img_cursor)
bt_personagem5 = bt.Botao(img_quadro, 150, 635, 5, img_cursor)

bt_personagem_lista  = [bt_personagem1, bt_personagem2, bt_personagem3, bt_personagem4, bt_personagem5]

img_amigo = pygame.image.load("imagem/personagem/amigo/0.png").convert_alpha()
img_amigo_rect = img_amigo.get_rect(center=(150, 135))

img_rogerio = pygame.image.load("imagem/personagem/rogerio/0.png").convert_alpha()
img_rogerio_rect = img_rogerio.get_rect(center=(360, 135))

img_ico = pygame.image.load("imagem/personagem/ico/0.png").convert_alpha()
img_ico_rect = img_ico.get_rect(center=(150, 385))

img_bicho = pygame.image.load("imagem/personagem/bicho/0.png").convert_alpha()
img_bicho_rect = img_bicho.get_rect(center=(360, 385))

img_adiburai = pygame.image.load("imagem/personagem/adiburai/0.png").convert_alpha()
img_adiburai_rect = img_adiburai.get_rect(center=(150, 635))

icone_lista = [img_amigo, img_rogerio, img_ico, img_bicho, img_adiburai]

def tela_selecao():
    clicou = False
    indice = 1


    while(True):
        
        # Clock
        clock.tick(fps)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicou = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if event.key == pygame.K_UP:
                    indice -= 2
                if event.key == pygame.K_DOWN:
                    indice += 2


        # Atualizacao
        
        if indice > 6: 
            indice = 1
        if indice < 1: 
            indice = 5
        """
        if clicou:
            for bt in bt_personagem_lista:
                bt.checkForInput(pygame.mouse.get_pos())
                
            clicou = False

        """

        # Renderizacao

        janela.blit(img_fundo, (0,0))

        for bt in bt_personagem_lista:
            bt.update(janela)
            bt.desenharCursor(janela, indice)

        
        janela.blit(img_amigo, img_amigo_rect)
        janela.blit(img_rogerio, img_rogerio_rect)
        janela.blit(img_bicho, img_bicho_rect)
        janela.blit(img_ico, img_ico_rect)
        janela.blit(img_adiburai, img_adiburai_rect)


        pygame.display.flip()

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

        pygame.display.flip()

tela_selecao()