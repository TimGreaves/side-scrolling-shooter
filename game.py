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

    def get_shot_location(self):
        return (self._x + 20, self._y + 20)


class Shot(object):

    def __init__(self, start_location):
        self._position = start_location    
   
    def get_position(self):
        return self._position

    def update_position(self):
        self._position = (self._position[0] + 2, self._position[1])

    def out_of_bounds(self, width):
        return self._position[0] > width


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
    for s in shots:
        screen.blit(shot_image, s.get_position())
    pygame.display.update()

def fire_shot():
    shot_location = player.get_shot_location()
    new_shot = Shot(shot_location)
    shots.append(new_shot)

def update_shots():
    for s in shots:
        s.update_position()
        if s.out_of_bounds(640):
            shots.remove(s)

pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player_image = pygame.image.load("resources/PlayerShip.png")
player = PlayerShip(0, 0, width, height, player_image.get_height(), player_image.get_width())

shot_image = pygame.image.load("resources/Shot.png")
shots = []

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
    if pressed_keys[pygame.K_SPACE]:
        fire_shot()

    update_shots()   
    update_screen()

