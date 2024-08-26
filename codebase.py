import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1540, 830
FPS = 60
PLAYER_VEL = 5
vidas = -5
vivo=True
window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size) #Aqui es donde salen el terreno quiero las coordenadas de los otros, ve el video para que entiendas mejor
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_block2(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size) #Aqui es donde salen el terreno quiero las coordenadas de los otros, ve el video para que entiendas mejor
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 4

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x, ):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x, ):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Plataform(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block2(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x, ):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x, )

    player.draw(window, offset_x, )

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Background.png")

    block_size = 96
    block_size2 = 48

    player = Player(100, 100, 50, 50)
    
    fire = Fire(block_size * 14.7, HEIGHT - block_size - 64, 16, 32)
    
    fire.on(),
    

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor,
                #Bloques del tutorial
                Block(block_size * 15, HEIGHT - block_size * 2, block_size),
                Block(block_size * 22, HEIGHT - block_size * 2, block_size),
                Block(block_size * 22, HEIGHT - block_size * 3, block_size),
                Block(block_size * 31, HEIGHT - block_size * 2, block_size),
                Block(block_size * 31, HEIGHT - block_size * 3, block_size),
                Block(block_size * 33, HEIGHT - block_size * 1, block_size),
                Block(block_size * 34, HEIGHT - block_size * 1, block_size),
                Block(block_size * 35, HEIGHT - block_size * 1, block_size),
                Block(block_size * 36, HEIGHT - block_size * 1, block_size),
                Block(block_size * 37, HEIGHT - block_size * 1, block_size),
                Block(block_size * 38, HEIGHT - block_size * 1, block_size),
                Block(block_size * 40, HEIGHT - block_size * 1, block_size),
                Block(block_size * 42, HEIGHT - block_size * 1, block_size),
                Block(block_size * 43, HEIGHT - block_size * 1, block_size),
                Block(block_size * 60, HEIGHT - block_size * 1, block_size),
                Block(block_size * 61, HEIGHT - block_size * 1, block_size),
                Block(block_size * 62, HEIGHT - block_size * 1, block_size),
                Block(block_size * 63, HEIGHT - block_size * 1, block_size),
                Block(block_size * 64, HEIGHT - block_size * 1, block_size),
                Block(block_size * 65, HEIGHT - block_size * 1, block_size),
                Block(block_size * 66, HEIGHT - block_size * 1, block_size),
                Block(block_size * 67, HEIGHT - block_size * 1, block_size),
                Plataform(block_size2 * 90, HEIGHT - block_size2 * 5, block_size2),
                Plataform(block_size2 * 91, HEIGHT - block_size2 * 5, block_size2),
                Plataform(block_size2 * 93, HEIGHT - block_size2 * 9, block_size2),
                Plataform(block_size2 * 94, HEIGHT - block_size2 * 9, block_size2),
                Plataform(block_size2 * 95, HEIGHT - block_size2 * 9, block_size2),
                Plataform(block_size2 * 98, HEIGHT - block_size2 * 13, block_size2),
                Plataform(block_size2 * 99, HEIGHT - block_size2 * 13, block_size2),
                Plataform(block_size2 * 100, HEIGHT - block_size2 * 13, block_size2),
                Plataform(block_size2 * 108, HEIGHT - block_size2 * 11, block_size2),
                Plataform(block_size2 * 109, HEIGHT - block_size2 * 11, block_size2),
                Plataform(block_size2 * 113, HEIGHT - block_size2 * 11, block_size2),
                Plataform(block_size2 * 114, HEIGHT - block_size2 * 11, block_size2),
                Plataform(block_size2 * 115, HEIGHT - block_size2 * 10, block_size2),
                Plataform(block_size2 * 116, HEIGHT - block_size2 * 9, block_size2),
                Plataform(block_size2 * 121, HEIGHT - block_size2 * 12, block_size2),
                Plataform(block_size2 * 124, HEIGHT - block_size2 * 12, block_size2),
                Plataform(block_size2 * 128, HEIGHT - block_size2 * 12, block_size2), Plataform(block_size2 * 130, HEIGHT - block_size2 * 12, block_size2), Plataform(block_size2 * 134, HEIGHT - block_size2 * 12, block_size2),Plataform(block_size2 * 138, HEIGHT - block_size2 * 12, block_size2),
                Plataform(block_size2 * 147, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 148, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 149, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 150, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 151, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 152, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 153, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 154, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 155, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 156, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 157, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 158, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 159, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 160, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 163, HEIGHT - block_size2 * 8, block_size2),
                Plataform(block_size2 * 164, HEIGHT - block_size2 * 9, block_size2),
                Plataform(block_size2 * 165, HEIGHT - block_size2 * 10, block_size2),
                Plataform(block_size2 * 166, HEIGHT - block_size2 * 11, block_size2),
                Plataform(block_size2 * 167, HEIGHT - block_size2 * 12, block_size2),
                Plataform(block_size2 * 168, HEIGHT - block_size2 * 13, block_size2),
                Plataform(block_size2 * 169, HEIGHT - block_size2 * 14, block_size2),
                Plataform(block_size2 * 170, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 171, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 172, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 180, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 181, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 189, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 190, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 198, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 199, HEIGHT - block_size2 * 15, block_size2),
                Plataform(block_size2 * 209, HEIGHT - block_size2 * 7, block_size2),
               
                fire]

    offset_x = 0
    
    scroll_area_width = 200
    
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x, )

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
            #lo de la camara debe ser aca (para subirla)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    for i in range (vidas,1):
        while vivo==True:
            main(window)
