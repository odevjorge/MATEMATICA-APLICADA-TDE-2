import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Movendo Quadrado com Reflexo')

# Coordenadas iniciais do quadrado
x_quadrado = largura // 2
y_quadrado = altura // 2
lado_quadrado = 50

# Coordenadas da parede
x_parede = largura // 4
y_parede = altura // 3
largura_parede = 10
altura_parede = altura // 3

# Velocidade do movimento
velocidade = 5

# Cor do quadrado
cor_quadrado = (0, 0, 255)

# Cor do quadrado reflexo
cor_quadrado_reflexo = (255, 0, 0)

# Variável para rastrear se o botão do mouse está pressionado
mouse_pressionado = False

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_pressionado = True
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            mouse_pressionado = False

    # Obtenha a posição do mouse
    pos_mouse = pygame.mouse.get_pos()
    x_mouse, y_mouse = pos_mouse

    # Mova o quadrado se o botão do mouse estiver pressionado
    if mouse_pressionado:
        x_quadrado = x_mouse
        y_quadrado = y_mouse

    # Verifique se o quadrado está próximo da parede
    proximo_a_parede = (x_quadrado > x_parede - lado_quadrado and x_quadrado < x_parede + largura_parede)

    # Preencha a tela com uma cor de fundo
    tela.fill((255, 255, 255))

    # Desenhe a parede
    pygame.draw.rect(tela, (0, 0, 0), (x_parede, y_parede, largura_parede, altura_parede))

    # Desenhe o quadrado
    pygame.draw.rect(tela, cor_quadrado, (x_quadrado - lado_quadrado / 2, y_quadrado - lado_quadrado / 2, lado_quadrado, lado_quadrado))

    # Se o quadrado estiver próximo da parede, desenhe o quadrado reflexo
    if proximo_a_parede:
        x_reflexo = 2 * x_parede + largura_parede - x_quadrado
        pygame.draw.rect(tela, cor_quadrado_reflexo, (x_reflexo - lado_quadrado / 2, y_quadrado - lado_quadrado / 2, lado_quadrado, lado_quadrado))

    # Atualize a tela
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()

# Encerre o programa
sys.exit()
