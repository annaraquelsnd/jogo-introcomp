import pygame
import botao as bt
import personagem as ps

pygame.init()

# Defines
clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

vida_max = 100

# Imagem de fundo
img_fundo = pygame.image.load("images/background/bg_batalha.png").convert_alpha()
img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

# Classe botão
img_quadro = pygame.image.load("images/icon/btSelect.png").convert_alpha()
img_quadro = pygame.transform.scale(img_quadro, (altura/4, altura/4))

img_cursor = pygame.image.load("images/icon/cursor.png").convert_alpha()
img_cursor = pygame.transform.scale(img_cursor, (largura/20, altura/20))

bt_personagem1 = bt.Botao(img_quadro, 277, 322, 1, img_cursor, True)
bt_personagem2 = bt.Botao(img_quadro, 512, 322, 2, img_cursor, True)
bt_personagem3 = bt.Botao(img_quadro, 747, 322, 3, img_cursor, True)
bt_personagem4 = bt.Botao(img_quadro, 395, 580, 4, img_cursor, True)
bt_personagem5 = bt.Botao(img_quadro, 630, 580, 5, img_cursor, True)

# Lista de botões dos personagens
bt_personagem_lista = [bt_personagem1, bt_personagem2, bt_personagem3, bt_personagem4, bt_personagem5]

# Botão para iniciar batalha
img_play = pygame.image.load("images/icon/playCinza.png").convert_alpha()
img_play = pygame.transform.scale(img_play, (altura/20, largura/20))
img_play_verde = pygame.image.load("images/icon/play.png").convert_alpha()
img_play_verde = pygame.transform.scale(img_play_verde, (altura/20, largura/20))
bt_play = bt.Botao(img_play, 985, 730, 6, img_play_verde, False)

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
hunter = ps.Personagem("Hunter", img_hunter, 0, 0, vida_max, 30, 30)
paladino = ps.Personagem("Paladino", img_paladino, 0, 0, vida_max, 30, 30)
priest = ps.Personagem("Priest", img_priest, 0, 0, vida_max, 30, 30)
rogue = ps.Personagem("Rogue", img_rogue, 0, 0, vida_max, 30, 30)
wizard = ps.Personagem("Wizard", img_wizard, 0, 0, vida_max, 30, 30)

# - Atribuicao de um personagem para cada botão
bt_personagem1.personagem = hunter
bt_personagem2.personagem = paladino
bt_personagem3.personagem = priest
bt_personagem4.personagem = rogue
bt_personagem5.personagem = wizard

# Lista de personagens selecionados pelo jogador
personagens_selecionados = []

def telaInicio():
    pygame.display.set_caption("IntroBattle")
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
                    if (indice == 1):
                        indice += 3
                    else:
                        indice +=2
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

            # Clicar no botão play
            if bt_play.checkInputCursor(indice) and len(personagens_selecionados) == 3:
                # Começar batalha
                definir_posicao()
                batalha()

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

        pos_x_selecionados = 930
        pos_y_selecionados = 745

        # Render dos personagens selecionados pelo jogador
        for personagem in personagens_selecionados:
            rect = personagem.imagem.get_rect(center=(pos_x_selecionados,pos_y_selecionados))
            janela.blit(pygame.transform.scale(personagem.imagem, (64, 64)), rect)
            pos_x_selecionados -= 55

        # Render do botao play
        bt_play.update(janela)
        bt_play.desenharCursor(janela, indice)

        pygame.display.update()

# BATALHA

img_painel_acoes = pygame.image.load("images/icon/panelActions.png").convert_alpha()
img_painel_acoes = pygame.transform.scale(img_painel_acoes, (largura, altura))

img_painel_vidas = pygame.image.load("images/icon/panelLifes.png").convert_alpha()
img_painel_vidas = pygame.transform.scale(img_painel_vidas, (largura, altura))

pygame.font.init()
fonte = pygame.font.Font("fonte/pixel.ttf", 24)

img_inimigo1 = pygame.image.load("images/character/inimigo1.png").convert_alpha()
img_inimigo1 = pygame.transform.scale(img_inimigo1, (96, 96))
img_inimigo2 = pygame.image.load("images/character/inimigo2.png").convert_alpha()
img_inimigo2 = pygame.transform.scale(img_inimigo2, (96, 96))

inimigo1 = ps.Personagem("Inimigo 1", img_inimigo1, 0, 0, 100, 30, 10)
inimigo2 = ps.Personagem("Inimigo 2", img_inimigo2, 0, 0, 100, 30, 10)

img_vida_borda = pygame.image.load("images/icon/life-indicator-null.png").convert_alpha()
img_vida_verde = pygame.image.load("images/icon/life-indicator-green.png").convert_alpha()
img_vida_amarelo = pygame.image.load("images/icon/life-indicator-yellow.png").convert_alpha()
img_vida_vermelho = pygame.image.load("images/icon/life-indicator-red.png").convert_alpha()

ordem = []
nomes = []

def batalha():

    pygame.display.set_caption("IntroBattle - Batalha")

    for ps in personagens_selecionados:
        nomes.append(fonte.render(ps.nome, True, "black"))

    ordem.extend(personagens_selecionados)
    ordem.extend([inimigo1, inimigo2])
    
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

        # - Desenhando os personagens na tela
        for ps in personagens_selecionados:
            if (ps.vida > 0):
                ps.update(janela)

        if inimigo1.vida > 0:
            inimigo1.update(janela)
        if inimigo2.vida > 0:
            inimigo2.update(janela)

        janela.blit(img_painel_acoes, (0,0))

        # - Painel de vida 
        janela.blit(img_painel_vidas, (0,0))

        y_nome = 545
        for nome in nomes:
            janela.blit(nome, (620, y_nome))
            y_nome += 65

        y_vida = 555
        for ps in personagens_selecionados:
            janela.blit(img_vida_borda, (796, y_vida))
            if (ps.vida >= 60):
                janela.blit(pygame.transform.scale(img_vida_verde, ((ps.vida/vida_max)*174, 14)), (801, y_vida+5))
            elif (ps.vida >= 20):
                janela.blit(pygame.transform.scale(img_vida_amarelo, ((ps.vida/vida_max)*174, 14)), (801, y_vida+5))
            else:
                janela.blit(pygame.transform.scale(img_vida_vermelho, ((ps.vida/vida_max)*174, 14)), (801, y_vida+5))

            y_vida += 65

        pygame.display.flip()

def definir_posicao():
    personagens_selecionados[0].setPosicao(190, 240)
    personagens_selecionados[1].setPosicao(80, 340)
    personagens_selecionados[2].setPosicao(190, 440)

    inimigo1.setPosicao(830, 240)
    inimigo2.setPosicao(770, 400)

telaInicio()