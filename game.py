import sys
import pygame

class PlayerShip(object):

    def __init__(self, start_x, start_y):
        self._x = start_x
        self._y = start_y

    def move_up(self):
        self._y -= 1

    def move_down(self):
        self._y += 1

    def move_left(self):
        self._x -= 1

    def move_right(self):
        self._x += 1

    def get_position(self):
        return (self._x, self._y)



pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player_image = pygame.image.load("resources/PlayerShip.png")
player = PlayerShip(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        player.move_up()
    if pressed_keys[pygame.K_DOWN]:
        player.move_down()
    if pressed_keys[pygame.K_LEFT]:
        player.move_left()
    if pressed_keys[pygame.K_RIGHT]:
        player.move_right()
   
    screen.fill(black)
    screen.blit(player_image, player.get_position())
    pygame.display.flip()
