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
    
    screen.fill(black)
    screen.blit(player, player_rect)
    pygame.display.flip()
