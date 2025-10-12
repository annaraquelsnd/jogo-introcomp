import pygame

class Botao():
    def __init__(self, image, x_pos, y_pos, indice, img_cursor, personagem):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.indice = indice
        self.img_cursor = img_cursor

        if personagem: 
            self.img_cursor_rect = img_cursor.get_rect(center=(x_pos, self.rect.y))
        else:
            self.img_cursor_rect = img_cursor.get_rect(center=(x_pos, y_pos))

    # Render do botao
    def update(self, janela):
        janela.blit(self.image, self.rect)
    
    # Desenha o cursor sobre o botão
    def desenharCursor(self, janela, indice):
        if indice == self.indice:
            janela.blit(self.img_cursor, self.img_cursor_rect)
            
    # Método chamado para verificar se o botão está envolvido na interação
    def checkInputCursor(self, indice):
          if indice == self.indice:
                return True