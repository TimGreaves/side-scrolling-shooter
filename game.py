import sys
import pygame

class PlayerShip(pygame.sprite.Sprite):

    SPEED = 3

    def __init__(self, image, start_pos, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = start_pos
        self._bounds = bounds
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_up:
            self.rect.top = max(self.rect.top - PlayerShip.SPEED, 0)
        if self.moving_down:
            self.rect.bottom = min(self.rect.bottom + PlayerShip.SPEED, self._bounds[1])
        if self.moving_left:
            self.rect.left = max(self.rect.left - PlayerShip.SPEED, 0)
        if self.moving_right:
            self.rect.right = min(self.rect.right + PlayerShip.SPEED, self._bounds[0])

    def get_shot_location(self):
        return (self.rect.right, self.rect.centery)


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
    sprites.draw(screen)
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
player = PlayerShip(player_image, (0, 0), (width, height))
sprites = pygame.sprite.Group()
sprites.add(player)
clock = pygame.time.Clock()

shot_image = pygame.image.load("resources/Shot.png")
shots = []
shot_timer = 0

while True:
    process_events()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LCTRL]:
        fire_shot()

    sprites.update()
    update_shots()
    
    update_screen()

    clock.tick(60)
