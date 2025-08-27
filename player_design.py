import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.image = pygame.image.load("Pirate Ship Image.png")
        new_player_size = (100,100)
        self.image = pygame.transform.scale(self.image, new_player_size)
        self.rect = self.image.get_rect()
        self.rect.center = (window_width // 2, window_height // 2)
        self.speed = 5  # single speed value

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
