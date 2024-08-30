import os
import random
import math
import pygame
import Clases
import Funciones
from os import listdir
from os.path import isfile, join
pygame.init()


pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1540, 830
FPS = 60
PLAYER_VEL = 7
vidas = -5
vivo=True
window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = Funciones.get_background("Background.png")

    block_size = 96
    block_size2 = 48

    player = Clases.Player(100, 100, 50, 50)
    
    fire = Clases.Fire(block_size * 14.7, HEIGHT - block_size - 64, 16, 32)
    fire2 = Clases.Fire(block_size * 16, HEIGHT - block_size - 64, 16, 32)
    fire.on(),
    fire2.on(),

    floor = [Clases.Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor,
                #Bloques del tutorial
                Clases.Block(block_size * 15, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 22, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 22, HEIGHT - block_size * 3, block_size),
                Clases.Block(block_size * 31, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 31, HEIGHT - block_size * 3, block_size),
                Clases.Block(block_size * 33, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 34, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 35, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 36, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 37, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 38, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 40, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 42, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 43, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 60, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 61, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 62, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 63, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 64, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 65, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 66, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 67, HEIGHT - block_size * 1, block_size),
                Clases.Plataform(block_size2 * 90, HEIGHT - block_size2 * 5, block_size2),
                Clases.Plataform(block_size2 * 91, HEIGHT - block_size2 * 5, block_size2),
                Clases.Plataform(block_size2 * 93, HEIGHT - block_size2 * 9, block_size2),
                Clases.Plataform(block_size2 * 94, HEIGHT - block_size2 * 9, block_size2),
                Clases.Plataform(block_size2 * 95, HEIGHT - block_size2 * 9, block_size2),
                Clases.Plataform(block_size2 * 98, HEIGHT - block_size2 * 13, block_size2),
                Clases.Plataform(block_size2 * 99, HEIGHT - block_size2 * 13, block_size2),
                Clases.Plataform(block_size2 * 100, HEIGHT - block_size2 * 13, block_size2),
                Clases.Plataform(block_size2 * 108, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 109, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 113, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 114, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 115, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 116, HEIGHT - block_size2 * 9, block_size2),
                Clases.Plataform(block_size2 * 121, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 124, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 128, HEIGHT - block_size2 * 12, block_size2), Clases.Plataform(block_size2 * 130, HEIGHT - block_size2 * 12, block_size2), Clases.Plataform(block_size2 * 134, HEIGHT - block_size2 * 12, block_size2),Clases.Plataform(block_size2 * 138, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 147, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 148, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 149, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 150, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 151, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 152, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 153, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 154, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 155, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 156, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 157, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 158, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 159, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 160, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 163, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 164, HEIGHT - block_size2 * 9, block_size2),
                Clases.Plataform(block_size2 * 165, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 166, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 167, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 168, HEIGHT - block_size2 * 13, block_size2),
                Clases.Plataform(block_size2 * 169, HEIGHT - block_size2 * 14, block_size2),
                Clases.Plataform(block_size2 * 170, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 171, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 172, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 180, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 181, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 189, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 190, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 198, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 199, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 209, HEIGHT - block_size2 * 7, block_size2),
                fire2,
                fire]

    offset_x = 0
    
    scroll_area_width = 900
    
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
        fire2.loop()
        Funciones.handle_move(player, objects)
        Funciones.draw(window, background, bg_image, player, objects, offset_x, )

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
