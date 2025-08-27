import pygame

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Treasure Chest Image.png")
        treasure_chest_new_size = (90,90)
        self.image = pygame.transform.scale(self.image, treasure_chest_new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass  
