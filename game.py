import sys
import pygame

class PlayerShip(object):

    SPEED = 3

    def __init__(self, start_x, start_y, max_x, max_y, ship_height, ship_width):
        self._x = start_x
        self._y = start_y
        self._max_x = max_x
        self._max_y = max_y
        self._ship_height = ship_height
        self._ship_width = ship_width
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def move_up(self):
        self._y -= PlayerShip.SPEED

    def move_down(self):
        self._y += PlayerShip.SPEED

    def move_left(self):
        self._x -= PlayerShip.SPEED

    def move_right(self):
        self._x += PlayerShip.SPEED

    def update(self):
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()

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
        self._position = (self._position[0] + 4, self._position[1])

    def out_of_bounds(self, width):
        return self._position[0] > width


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.moving_up = True
            elif event.key == pygame.K_DOWN:
                player.moving_down = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.moving_up = False        
            elif event.key == pygame.K_DOWN:
                player.moving_down = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_RIGHT:
                player.moving_right = False

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
    global shot_timer
    if shot_timer > 0:
        return
    shot_location = player.get_shot_location()
    new_shot = Shot(shot_location)
    shots.append(new_shot)
    shot_timer = 8

def update_shots():
    global shot_timer
    shot_timer -= 1
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
clock = pygame.time.Clock()

shot_image = pygame.image.load("resources/Shot.png")
shots = []
shot_timer = 0

while True:
    process_events()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LCTRL]:
        fire_shot()

    player.update()
    update_shots()
    
    update_screen()

    clock.tick(60)
