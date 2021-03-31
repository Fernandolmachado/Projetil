import pygame


def get_sprites(rectangle):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

# janela
WIDTH = 800
HEIGHT = 600
pygame.display.set_caption("Projetil")
janela = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = pygame.Color(255, 255, 255)
background_image = pygame.image.load("img/background_forest.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# FPS
clock = pygame.time.Clock()
fps = 60


# jogador
sheet = pygame.image.load("img/player.png").convert()
images_right = [get_sprites([i, 0, 200, sheet.get_height()]) for i in range(0, 600, 200)]
images_left = [get_sprites([i, 0, 200, sheet.get_height()]) for i in range(600, 1200, 200)]

player_width = 50
player_height = 75

for i in range(3):
    images_left[i] = pygame.transform.scale(images_left[i], (player_width, player_height))
    images_right[i] = pygame.transform.scale(images_right[i], (player_width, player_height))

indice = 0
contador = 0
animacao = 5
velocidade = [5, 0]
posicao = [0, HEIGHT - player_height - 60]
direcao = 0

player = images_right[indice]

funcionando = True

# loop principal
while funcionando:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            funcionando = False

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_RIGHT] and contador >= animacao:
            contador = 0
            indice = (indice + 1) % 3
            player = images_right[indice]
            posicao[0] += velocidade[0]
            direcao = 0
    elif tecla[pygame.K_LEFT] and contador >= animacao:
            contador = 0
            indice = (indice + 1) % 3
            posicao[0] -= velocidade[0]
            player = images_left[indice]
            direcao = 1
    else:
        if contador >= animacao:
            indice = 0
            if direcao == 0:
                player = images_right[indice]
            else:
                player = images_left[indice]

    if tecla[pygame.K_SPACE]:
        player = pygame.transform.rotate()

    contador += 1
    janela.fill(background_color)
    janela.blit(background_image, (0, 0))
    janela.blit(player, posicao)
    pygame.display.update()
