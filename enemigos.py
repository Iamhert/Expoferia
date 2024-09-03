import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, x,y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x,y))
        
