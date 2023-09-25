import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ajuste de Escala com a Roda do Mouse')

# Coordenadas iniciais do objeto
x_objeto, y_objeto = largura // 2, altura // 2

# Fator de escala inicial
escala = 1.0

# Imagem do objeto (substitua por sua própria imagem, se desejar)
objeto_imagem = pygame.Surface((50, 50))
objeto_imagem.fill((0, 0, 255))

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        # Verifique se o evento é um evento de rolagem do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 4:
            escala *= 1.1  # Aumenta a escala em 10%
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 5:
            escala /= 1.1  # Diminui a escala em 10%

    # Preencha a tela com uma cor de fundo
    tela.fill((255, 255, 255))

    # Realize a escala do objeto
    objeto_escala = pygame.transform.scale(objeto_imagem, (int(objeto_imagem.get_width() * escala), int(objeto_imagem.get_height() * escala)))

    # Obtém o retângulo da imagem escalada
    objeto_retangulo = objeto_escala.get_rect()

    # Define a posição do objeto escalado
    objeto_retangulo.center = (x_objeto, y_objeto)

    # Desenhe o objeto escalado
    tela.blit(objeto_escala, objeto_retangulo.topleft)

    # Atualize a tela
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()

# Encerre o programa
sys.exit()
