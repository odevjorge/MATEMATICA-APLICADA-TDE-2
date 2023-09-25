import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Translação de Objeto')

# Defina as coordenadas iniciais do objeto
x_objeto, y_objeto = largura // 2, altura // 2

# Defina a velocidade da translação
velocidade = 5

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Obtenha as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Atualize as coordenadas do objeto com base nas teclas pressionadas
    if teclas[pygame.K_LEFT]:
        x_objeto -= velocidade
    if teclas[pygame.K_RIGHT]:
        x_objeto += velocidade
    if teclas[pygame.K_UP]:
        y_objeto -= velocidade
    if teclas[pygame.K_DOWN]:
        y_objeto += velocidade

    # Preencha a tela com uma cor de fundo
    tela.fill((255, 255, 255))

    # Desenhe o objeto na nova posição
    pygame.draw.rect(tela, (0, 0, 255), (x_objeto, y_objeto, 50, 50))

    # Atualize a tela
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()

# Encerre o programa
sys.exit()
