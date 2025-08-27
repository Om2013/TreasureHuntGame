import pygame

class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x=3, speed_y=3):
        super().__init__()
        self.image = pygame.image.load("Shark Image.png")
        shark_new_size = (95,95)
        self.image = pygame.transform.scale(self.image, shark_new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def update(self):
        # Move shark
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off screen edges
        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1  # Reverse horizontal direction
        
        if self.rect.bottom > 600 or self.rect.top < 0:
            self.speed_y *= -1  # Reverse vertical direction
