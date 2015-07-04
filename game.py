import sys
import pygame

pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player = pygame.image.load("resources/PlayerShip.png")
player_rect = player.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        player_rect = player_rect.move(0, -1)
    if pressed_keys[pygame.K_DOWN]:
        player_rect = player_rect.move(0, 1)
    if pressed_keys[pygame.K_LEFT]:
        player_rect = player_rect.move(-1, 0)
    if pressed_keys[pygame.K_RIGHT]:
        player_rect = player_rect.move(1, 0)
    
    screen.fill(black)
    screen.blit(player, player_rect)
    pygame.display.flip()
