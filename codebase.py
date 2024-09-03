import os
import random
import math
import time
import pygame
import Clases
import Funciones
import enemigos, fires
from os import listdir
from os.path import isfile, join
pygame.init()


pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
WIDTH, HEIGHT = 1540, 830
FPS = 60
vidas = -5
window = pygame.display.set_mode((WIDTH, HEIGHT))

#enemy = enemigos.Enemy(100,100,32,32)


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = Funciones.get_background("Background.png")
    backgroundd, bg_imaged = Funciones.get_background("Backgroundd.png")
    block_size = 96
    block_size2 = 48

    player = Clases.Player(100, 100, 50, 50)
   
    #enemies = pygame.sprite.Group()
    #enemies.add(enemy)
    
    fires.fire.on(),fires.fire2.on(),fires.fire3.on(),fires.fire4.on(),fires.fire5.on(),fires.fire6.on(),fires.fire7.on(),fires.fire8.on(),fires.fire9.on(),

    floor = [Clases.Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    floor2 = [Clases.BlockD(i * block_size, 1000 - block_size, block_size)
             for i in range(-5000 // block_size, (7000 * 2) // block_size)]
    objects = [*floor,*floor2,
                
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
                Clases.Plataform(block_size2 * 215, HEIGHT - block_size2 * 7, block_size2),
                Clases.Plataform(block_size2 * 216, HEIGHT - block_size2 * 7, block_size2),
                Clases.Plataform(block_size2 * 224, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 225, HEIGHT - block_size2 * 11, block_size2),
                Clases.Plataform(block_size2 * 234, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 235, HEIGHT - block_size2 * 15, block_size2),
                Clases.Block(block_size * 127, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 128, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 129, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 130, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 133, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 134, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 135, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 136, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 137, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 138, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 139, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 143, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 144, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 145, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 146, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 146, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 146, HEIGHT - block_size * 3, block_size),
                Clases.Block(block_size * 147, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 148, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 149, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 150, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 151, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 152, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 153, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 154, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 155, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 156, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 157, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 158, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 159, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 160, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 160, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 160, HEIGHT - block_size * 3, block_size),
                Clases.Plataform(block_size2 * 300, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 301, HEIGHT - block_size2 * 10, block_size2),
                 Clases.Plataform(block_size2 * 311, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 312, HEIGHT - block_size2 * 10, block_size2),
                fires.fire,fires.fire2, fires.fire3, fires.fire4, fires.fire5,fires.fire7,fires.fire8,fires.fire9
                ]

    offset_x = 0
    
    scroll_area_width = 900
    
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if player.hit==True :
                Funciones.daño-=1
                if Funciones.daño ==0:
                    Funciones.PLAYER_VEL=0
                    Clases.Player.GRAVITY=0
                    Funciones.dead(window, backgroundd, bg_imaged, )
                    time.sleep(2)
                    run=False
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        pygame.display.update()
        player.loop(FPS)
        fires.fire.loop(),fires.fire2.loop(),fires.fire3.loop(),fires.fire4.loop(),fires.fire8.loop(),fires.fire5.loop(),fires.fire6.loop(),fires.fire7.loop(),fires.fire9.loop()
        Funciones.handle_move(player, objects, )
        Funciones.draw(window, background, bg_image, player, objects, offset_x,  )

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
            #camara
    
    
vivo=True

if __name__ == "__main__":
    for i in range (vidas,0):
        while vivo:
            fps = clock.get_fps()
            run=True
            main(window)
            vidas+=1
            Funciones.daño=3
            Funciones.PLAYER_VEL=10
            Clases.Player.GRAVITY=1
            pygame.quit()

            