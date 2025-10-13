import pygame

class Personagem():
    def __init__(self, nome, imagem, x_pos, y_pos, vida, ataque, defesa):
        self.nome = nome
        self.imagem = imagem
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    # Render do personagem na tela
    def update(self, janela):
        janela.blit(self.imagem, self.rect)

    # Utilizado para definir posição dos personagens no cenário de batalha
    def setPosicao(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos))
