import os
import random
import math
import time
import pygame
import Clases
import Funciones
import enemigos
import Traps
from os import listdir
from os.path import isfile, join
pygame.init()


pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
WIDTH, HEIGHT = 1540, 830
FPS = 60
vidas = -5
window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = Funciones.get_background("Background.png")
    
    block_size = 96
    block_size2 = 48

    player = Clases.Player(100, 100, 50, 50)
    
    
    Traps.fire.on(),Traps.fire2.on(),Traps.fire3.on(),Traps.fire4.on(),Traps.fire5.on(),Traps.fire6.on(),Traps.fire7.on(),Traps.fire8.on(),Traps.fire9.on(),
    Traps.fan.on(),Traps.fan2.on(),Traps.fan3.on(),Traps.fan4.on(),Traps.fan5.on(),Traps.fan6.on(),Traps.fan7.on(),Traps.fan8.on(),Traps.fan9.on(),Traps.fan10.on(),
    Traps.fan11.on(),Traps.fan12.on(),Traps.fan13.on(),Traps.fan14.on(),Traps.fan15.on(),Traps.fan16.on(),Traps.fan17.on(),Traps.fan18.on(),Traps.fan19.on(),Traps.fan20.on(),
    Traps.fan23.on(),Traps.fan24.on(),Traps.fan25.on(),Traps.fan26.on(),Traps.fan27.on(),Traps.fan28.on(),Traps.fan29.on(),Traps.fan30.on(),
    Traps.monster.on()
    floor = [Clases.Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    
    firefloor2 = [Clases.Fire(block_size * i, 1000 - block_size - 64, 16, 32)
                  for i in range(-5000 // block_size, (17000 * 2) // block_size)]
    objects = [*floor,                
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
                Clases.Plataform(block_size2 * 121, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 136, HEIGHT - block_size2 * 12, block_size2),
                Clases.Plataform(block_size2 * 147, HEIGHT - block_size2 * 8, block_size2),
                Clases.Plataform(block_size2 * 148, HEIGHT - block_size2 * 8, block_size2),
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
                Clases.Plataform(block_size2 * 186, HEIGHT - block_size2 * 15, block_size2),
                Clases.Plataform(block_size2 * 187, HEIGHT - block_size2 * 15, block_size2),
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
                 Clases.Block(block_size * 160, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 160, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 160, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 160, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 160, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 160, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 160, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 161, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 161, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 161, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 161, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 161, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 161, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 161, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 161, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 161, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 161, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 162, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 162, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 162, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 162, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 162, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 162, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 162, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 162, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 162, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 162, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 163, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 163, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 163, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 163, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 163, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 163, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 163, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 163, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 163, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 163, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 164, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 164, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 164, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 164, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 164, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 164, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 164, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 164, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 164, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 164, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 165, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 165, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 165, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 165, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 165, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 165, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 165, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 165, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 165, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 165, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 166, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 166, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 166, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 166, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 166, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 166, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 166, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 166, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 166, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 166, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 167, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 167, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 167, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 167, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 167, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 167, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 167, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 167, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 167, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 167, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 168, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 168, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 168, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 168, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 168, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 168, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 168, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 168, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 168, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 168, HEIGHT - block_size * 10, block_size),
                Clases.Block(block_size * 169, HEIGHT - block_size * 1, block_size),
                Clases.Block(block_size * 169, HEIGHT - block_size * 2, block_size),
                Clases.Block(block_size * 169, HEIGHT - block_size * 3, block_size),
                 Clases.Block(block_size * 169, HEIGHT - block_size * 4, block_size),
                  Clases.Block(block_size * 169, HEIGHT - block_size * 5, block_size),
                   Clases.Block(block_size * 169, HEIGHT - block_size * 6, block_size),
                    Clases.Block(block_size * 169, HEIGHT - block_size * 7, block_size),
                     Clases.Block(block_size * 169, HEIGHT - block_size * 8, block_size),
                      Clases.Block(block_size * 169, HEIGHT - block_size * 9, block_size),
                       Clases.Block(block_size * 169, HEIGHT - block_size * 10, block_size),                                            
                Clases.Plataform(block_size2 * 300, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 301, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 311, HEIGHT - block_size2 * 10, block_size2),
                Clases.Plataform(block_size2 * 312, HEIGHT - block_size2 * 10, block_size2),
                Traps.fire,Traps.fire2, Traps.fire3, Traps.fire4, Traps.fire5,Traps.fire7,Traps.fire8,Traps.fire9,*firefloor2,
                Traps.fan,Traps.fan2,Traps.fan3,Traps.fan4,Traps.fan5,Traps.fan6,Traps.fan7,Traps.fan8,Traps.fan9,Traps.fan10,
                Traps.fan11,Traps.fan12,Traps.fan13,Traps.fan14,Traps.fan15,Traps.fan16,Traps.fan17,Traps.fan18,Traps.fan19,Traps.fan20,
                Traps.fan23,Traps.fan24,Traps.fan25,Traps.fan26,Traps.fan27,Traps.fan28,Traps.fan29,Traps.fan30,
                Traps.monster
                ]

    offset_x = 0
    
    scroll_area_width = 900
    
    
    while Clases.Player.run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Clases.Player.run = False
                break
            
            if player.hit==True :
                Funciones.daño-=1
                if Funciones.daño ==0:
                    
                    Funciones.PLAYER_VEL=0
                    Clases.Player.GRAVITY=0
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    quit()
        pygame.display.update()
        player.loop(FPS)
        Traps.fire.loop(),Traps.fire2.loop(),Traps.fire3.loop(),Traps.fire4.loop(),Traps.fire8.loop(),Traps.fire5.loop(),Traps.fire6.loop(),Traps.fire7.loop(),Traps.fire9.loop(),
        Traps.fan.loop(),Traps.fan2.loop(),Traps.fan3.loop(),Traps.fan4.loop(),Traps.fan5.loop(),Traps.fan6.loop(),Traps.fan7.loop(),Traps.fan8.loop(),Traps.fan9.loop(),Traps.fan10.loop(),
        Traps.fan11.loop(),Traps.fan12.loop(),Traps.fan13.loop(),Traps.fan14.loop(),Traps.fan15.loop(),Traps.fan16.loop(),Traps.fan17.loop(),Traps.fan18.loop(),Traps.fan19.loop(),Traps.fan20.loop(),
        Traps.fan23.loop(),Traps.fan24.loop(),Traps.fan25.loop(),Traps.fan26.loop(),Traps.fan27.loop(),Traps.fan28.loop(),Traps.fan29.loop(),Traps.fan30.loop(),
        Traps.monster.loop()
        Funciones.handle_move(player, objects, )
        Funciones.draw(window, background, bg_image, player, objects, offset_x, )
        
        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
            #camara
    
    
vivo=True

if __name__ == "__main__":
    for i in range (vidas,0):
        while vivo:
            fps = clock.get_fps()
            Clases.Player.run=True
            main(window)
            vidas+=1
            Funciones.daño=3
            Funciones.PLAYER_VEL=10
            Clases.Player.GRAVITY=1
    pygame.quit()

            