import pygame
import sys
import math

# Inicialize o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Orbita de Quadrado Azul')

# Coordenadas do quadrado vermelho (no centro)
x_quadrado_vermelho = largura // 2 - 50
y_quadrado_vermelho = altura // 2 - 50
lado_quadrado_vermelho = 100

# Raio da órbita (distância do centro do quadrado vermelho ao centro do quadrado azul)
raio_orbita = 150

# Ângulo inicial da rotação do quadrado azul (em radianos)
angulo = 0

# Velocidade da rotação do quadrado azul (em radianos por frame)
velocidade_rotacao = math.radians(2) / 3

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Coordenadas do quadrado azul na órbita
    x_quadrado_azul = x_quadrado_vermelho + lado_quadrado_vermelho // 2 - 25 + raio_orbita * math.cos(angulo)
    y_quadrado_azul = y_quadrado_vermelho + lado_quadrado_vermelho // 2 - 25 + raio_orbita * math.sin(angulo)

    # Preencha a tela com uma cor de fundo
    tela.fill((255, 255, 255))

    # Desenhe o quadrado vermelho
    pygame.draw.rect(tela, (255, 0, 0), (x_quadrado_vermelho, y_quadrado_vermelho, lado_quadrado_vermelho, lado_quadrado_vermelho), 2)

    # Desenhe o quadrado azul na órbita
    pygame.draw.rect(tela, (0, 0, 255), (x_quadrado_azul, y_quadrado_azul, 50, 50), 2)

    # Atualize a tela
    pygame.display.flip()

    # Atualize o ângulo para a próxima iteração
    angulo += velocidade_rotacao

# Encerre o Pygame
pygame.quit()

# Encerre o programa
sys.exit()
