import time
from pygame.locals import *
import pygame

# Tamany finestra / Tamaño de la ventana
VIEW_WIDTH = 1280
VIEW_HEIGHT = 720

# iniciem pygame / Iniciamos pygame
pygame.init()
pantalla = pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT))
pygame.display.set_caption("Arcade")

# Carreguem imatge de fons / Cargamos imagen del fondo
background_image = 'assets/mapa-test.jpg'
background_width = pygame.image.load(background_image).convert().get_width()
background_height = pygame.image.load(background_image).convert().get_height()

# Límits per moure el fons enlloc del personatge / Limites para mover el fondo en vez del personaje
MARGIN_X, MARGIN_Y = VIEW_WIDTH // 2, VIEW_HEIGHT // 2

# Carreguem imatge inicial personatge / Cargamos la imagen inicial del jugador
player_image = pygame.image.load('assets/jugador/jugador-down-0.png')
protagonist_speed = 8

# Posicions inicials del personatge i del fons / Posiciones iniciales del personaje y del fondo
player_rect = player_image.get_rect(midbottom=(VIEW_WIDTH // 2, VIEW_HEIGHT // 2))
bg_x, bg_y = 0, 0

# Control de FPS
clock = pygame.time.Clock()
fps = 30

# Control de l'animació del personatge / control de la animación del personaje
# 1 up. 2 down. 3 right. 4 left
sprite_direction = "down"
sprite_index = 0
animation_protagonist_speed = 300
sprite_frame_number = 2
last_change_frame_time = 0
idle = False

# Pantalles del joc / Pantallas del juego
# Pantalla 1 --> Menú principal
# Pantalla 2 --> Explicación de controles --> Pulsar tecla "1"
# Pantalla 3 --> Menú de reglas del juego --> Pulsar tecla "2"
# Pantalla 4 --> Juego --> Pulsar tecla "espacio"
# Pantalla 5 --> Mundo del juego --> Salir de la casa
# Pantalla 6 --> Dentro de la "Casa" (tejado)

def imprimir_pantalla_fons(image, x, y):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current_time = pygame.time.get_ticks()

    # Moviment del jugador
    idle = True
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        idle = False
        sprite_direction = "up"
        if player_rect.y > MARGIN_Y or bg_y >= 0:
            player_rect.y = max(player_rect.y - protagonist_speed, player_rect.height // 2)
        else:
            bg_y = min(bg_y + protagonist_speed, 0)
    if keys[K_s]:
        idle = False
        sprite_direction = "down"
        if player_rect.y < VIEW_HEIGHT - MARGIN_Y or bg_y <= VIEW_HEIGHT - background_height:
            player_rect.y = min(player_rect.y + protagonist_speed, VIEW_HEIGHT - player_rect.height // 2)
        else:
            bg_y = max(bg_y - protagonist_speed, VIEW_HEIGHT - background_height)
    if keys[K_d]:
        idle = False
        sprite_direction = "right"
        if player_rect.x < VIEW_WIDTH - MARGIN_X or bg_x <= VIEW_WIDTH - background_width:
            player_rect.x = min(player_rect.x + protagonist_speed, VIEW_WIDTH - player_rect.width // 2)
        else:
            bg_x = max(bg_x - protagonist_speed, VIEW_WIDTH - background_width)
    if keys[K_a]:
        idle = False
        sprite_direction = "left"
        if player_rect.x > MARGIN_X or bg_x >= 0:
            player_rect.x = max(player_rect.x - protagonist_speed, player_rect.width // 2)
        else:
            bg_x = min(bg_x + protagonist_speed, 0)

    # Dibuixar el fons / Dibujar el fondo
    imprimir_pantalla_fons(background_image, bg_x, bg_y)

    #Moviment / Movimiento
    if not idle:
        if current_time - last_change_frame_time >= animation_protagonist_speed:
            last_change_frame_time = current_time
            sprite_index = sprite_index + 1
            if sprite_index >= sprite_frame_number:
                sprite_index = 0
            # Solo se intercalarán los frames de movimiento 1 y 2
            frame_to_use = sprite_index + 1
    else:
        frame_to_use = 0  #Está quieto

    # dibuixar el jugador
    player_image = pygame.image.load('assets/jugador/'"jugador-"+sprite_direction+"-"+str(frame_to_use)+'.png')
    pantalla.blit(player_image, player_rect)

    # mantenir el jugador dins la finestra
    player_rect.clamp_ip(pantalla.get_rect())

    pygame.draw.rect(pantalla,(255,255,0),(bg_x+100,bg_y+200,100,10))

    pygame.display.update()
    clock.tick(fps)