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


class Shot(pygame.sprite.Sprite):

    SPEED = 4

    def __init__(self, image, start_pos, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = start_pos
        self._bounds = bounds
   
    def update(self):
        self.rect.left += Shot.SPEED
        if self.rect.left > self._bounds[0]:
            self.kill()


class ShotManager(object):

    COOLDOWN_INTERVAL = 8

    def __init__(self, image, player, bounds):
        self._image = image
        self._player = player
        self._bounds = bounds
        self._shots = pygame.sprite.Group()
        self._cooldown = 0
        self.is_firing = False

    def fire_shot(self):
        shot_location = self._player.get_shot_location()
        new_shot = Shot(self._image, shot_location, self._bounds)
        self._shots.add(new_shot)
        self._cooldown = ShotManager.COOLDOWN_INTERVAL
        
    def update(self):
        self._cooldown = max(0, self._cooldown - 1)
        if self.is_firing and self._cooldown == 0:
            self.fire_shot()
        self._shots.update()

    def draw(self, surface):
        self._shots.draw(surface)


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == pygame.KEYDOWN:
            process_movement_keys(event.key, True)
            process_shot_keys(event.key, True)
        if event.type == pygame.KEYUP:
            process_movement_keys(event.key, False)
            process_shot_keys(event.key, False)

def process_movement_keys(key, is_key_down):
    if key == pygame.K_UP:
        player.moving_up = is_key_down
    elif key == pygame.K_DOWN:
        player.moving_down = is_key_down
    elif key == pygame.K_LEFT:
        player.moving_left = is_key_down
    elif key == pygame.K_RIGHT:
        player.moving_right = is_key_down

def process_shot_keys(key, is_key_down):
    if key == pygame.K_LCTRL:
        shot_manager.is_firing = is_key_down

def exit_game():
    pygame.quit()
    sys.exit()

def update_screen():
    screen.fill(black)
    sprites.draw(screen)    
    shot_manager.draw(screen)
    pygame.display.update()

     
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
shot_manager = ShotManager(shot_image, player, (width, height))

while True:
    process_events()

    sprites.update()
    shot_manager.update()
    
    update_screen()

    clock.tick(60)
