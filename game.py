import sys
import pygame

pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player = pygame.image.load("resources/PlayerShip.png")
player_x, player_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        player_y -= 1
    if pressed_keys[pygame.K_DOWN]:
        player_y += 1
    if pressed_keys[pygame.K_LEFT]:
        player_x -= 1
    if pressed_keys[pygame.K_RIGHT]:
        player_x += 1
   
    screen.fill(black)
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
