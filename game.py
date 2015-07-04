import sys
import pygame

class PlayerShip(object):

    SPEED = 1

    def __init__(self, start_x, start_y, max_x, max_y, ship_height, ship_width):
        self._x = start_x
        self._y = start_y
        self._max_x = max_x
        self._max_y = max_y
        self._ship_height = ship_height
        self._ship_width = ship_width

    def move_up(self):
        self._y -= PlayerShip.SPEED

    def move_down(self):
        self._y += PlayerShip.SPEED

    def move_left(self):
        self._x -= PlayerShip.SPEED

    def move_right(self):
        self._x += PlayerShip.SPEED

    def check_bounds(self):
        if self._x < 0:
            self._x = 0
        if self._x > self._max_x - self._ship_width:
            self._x = self._max_x - self._ship_width
        if self._y < 0:
            self._y = 0
        if self._y > self._max_y - self._ship_height:
            self._y = self._max_y - self._ship_height

    def get_position(self):
        self.check_bounds()
        return (self._x, self._y)




def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

def exit_game():
    pygame.quit()
    sys.exit()

def update_screen():
    screen.fill(black)
    screen.blit(player_image, player.get_position())
    pygame.display.update()



pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player_image = pygame.image.load("resources/PlayerShip.png")
player = PlayerShip(0, 0, width, height, player_image.get_height(), player_image.get_width())

while True:
    process_events()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        player.move_up()
    if pressed_keys[pygame.K_DOWN]:
        player.move_down()
    if pressed_keys[pygame.K_LEFT]:
        player.move_left()
    if pressed_keys[pygame.K_RIGHT]:
        player.move_right()
   
    update_screen()

