import pygame

class Personagem():
    def __init__(self, imagem, x_pos, y_pos, vida, ataque, defesa):
        self.imagem = imagem
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def update(self, janela):
        janela.blit(self.imagem, self.rect)