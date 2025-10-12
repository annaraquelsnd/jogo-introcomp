import pygame
import botao as bt
import personagem as ps

pygame.init()

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Batalha")

# Imagem de fundo
img_fundo = pygame.image.load("images/background/bg_batalha.png").convert_alpha()
img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

# Classe botão
img_quadro = pygame.image.load("images/icon/btSelect.png").convert_alpha()
img_quadro = pygame.transform.scale(img_quadro, (altura/4, altura/4))

img_cursor = pygame.image.load("images/icon/cursor.png").convert_alpha()
img_cursor = pygame.transform.scale(img_cursor, (largura/20, altura/20))

bt_personagem1 = bt.Botao(img_quadro, 277, 322, 1, img_cursor)
bt_personagem2 = bt.Botao(img_quadro, 512, 322, 2, img_cursor)
bt_personagem3 = bt.Botao(img_quadro, 747, 322, 3, img_cursor)
bt_personagem4 = bt.Botao(img_quadro, 395, 580, 4, img_cursor)
bt_personagem5 = bt.Botao(img_quadro, 630, 580, 5, img_cursor)

# - Lista de botões dos personagens
bt_personagem_lista = [bt_personagem1, bt_personagem2, bt_personagem3, bt_personagem4, bt_personagem5]

img_hunter = pygame.image.load("images/character/hunter.png").convert_alpha()
img_hunter = pygame.transform.scale(img_hunter, (96, 96))
img_hunter_rect = img_hunter.get_rect(center=(277, 322))
img_paladino = pygame.image.load("images/character/paladino.png").convert_alpha()
img_paladino = pygame.transform.scale(img_paladino, (96, 96))
img_paladino_rect = img_paladino.get_rect(center=(512, 322))
img_priest = pygame.image.load("images/character/priest.png").convert_alpha()
img_priest = pygame.transform.scale(img_priest, (96, 96))
img_priest_rect = img_priest.get_rect(center=(747, 322))
img_rogue = pygame.image.load("images/character/rogue.png").convert_alpha()
img_rogue = pygame.transform.scale(img_rogue, (96, 96))
img_rogue_rect = img_rogue.get_rect(center=(395, 580))
img_wizard = pygame.image.load("images/character/wizard.png").convert_alpha()
img_wizard = pygame.transform.scale(img_wizard, (96, 96))
img_wizard_rect = img_wizard.get_rect(center=(630, 580))

# - Lista de icones
icones_lista = [img_hunter, img_paladino, img_priest, img_rogue, img_wizard]

# - Declarando personagens
hunter = ps.Personagem(img_hunter, 0, 0, 100, 30, 30)
paladino = ps.Personagem(img_paladino, 0, 0, 100, 30, 30)
priest = ps.Personagem(img_priest, 0, 0, 100, 30, 30)
rogue = ps.Personagem(img_rogue, 0, 0, 100, 30, 30)
wizard = ps.Personagem(img_wizard, 0, 0, 100, 30, 30)

# - Atribuicao de um personagem para cada botão
bt_personagem1.personagem = hunter
bt_personagem2.personagem = paladino
bt_personagem3.personagem = priest
bt_personagem4.personagem = rogue
bt_personagem5.personagem = wizard

# Lista de personagens selecionados pelo jogador
personagens_selecionados = []

# Elementos batalha
img_painel_acoes = pygame.image.load("images/icon/panelActions.png").convert_alpha()
img_painel_acoes = pygame.transform.scale(img_painel_acoes, (largura, altura))

img_painel_vidas = pygame.image.load("images/icon/panelLifes.png").convert_alpha()
img_painel_vidas = pygame.transform.scale(img_painel_vidas, (largura, altura))

def telaInicio():

    pressionou = False
    indice = 1

    while(True):
        # Clock
        clock.tick(fps)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Navegação: mudança de posição do cursor
                if event.key == pygame.K_RIGHT:
                    indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if event.key == pygame.K_DOWN:
                    indice += 2
                if event.key == pygame.K_UP:
                    indice -= 2
                # Navegação: seleção do botão
                if event.key == pygame.K_z:
                    pressionou = True

        # Atualizacao

        # - Correcao do Indice
        if indice < 1:
            indice = 5
        elif indice > 6:
            indice = 1

        # - Adicionar/remover personagem da lista de selecionados
        if pressionou:
            for botao in bt_personagem_lista:
                if botao.checkInputCursor(indice):
                    if not (botao.personagem in personagens_selecionados):
                        if len(personagens_selecionados) < 3:
                            personagens_selecionados.append(botao.personagem)
                    else:
                        personagens_selecionados.remove(botao.personagem)

            # Adicinar evento de clicar no botão go

            pressionou = False

        # Renderizacao

        janela.blit(img_fundo, (0,0))

        for botao in bt_personagem_lista:
            botao.update(janela)
            botao.desenharCursor(janela, indice)

        janela.blit(img_hunter, img_hunter_rect)
        janela.blit(img_paladino, img_paladino_rect)
        janela.blit(img_priest, img_priest_rect)
        janela.blit(img_rogue, img_rogue_rect)
        janela.blit(img_wizard, img_wizard_rect)

        pygame.display.update()

def batalha():
    
    while(True):
        # Clock
        clock.tick(fps)

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Atualizacao


        # Renderizacao

        janela.blit(img_fundo, (0,0))
        janela.blit(img_painel_acoes, (0,0))
        janela.blit(img_painel_vidas, (0,0))
        pygame.display.flip()

telaInicio()