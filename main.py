# --------------------- Difficulty ---------------------
difficulty = input("Select difficulty (E=Easy, M=Medium, H=Hard, R=Random): ").strip().upper()

if difficulty == "R":
    import random
    difficulty = random.choice(["E", "M", "H"])
    print(f"Random difficulty chosen: {difficulty}")

if difficulty == "E":
    player_speed = 5
    lives = 3
    shark_speed = 3
    num_sharks = 2
    num_treasures = 5
elif difficulty == "M":
    player_speed = 6
    lives = 4
    shark_speed = 4
    num_sharks = 3
    num_treasures = 8
elif difficulty == "H":
    player_speed = 7
    lives = 5
    shark_speed = 6
    num_sharks = 5
    num_treasures = 12
else:
    print(f"Invalid input '{difficulty}', defaulting to Medium")
    player_speed = 6
    lives = 4
    shark_speed = 4
    num_sharks = 3
    num_treasures = 8

print(f"Difficulty: {difficulty}")
print(f"Player speed: {player_speed}, Shark speed: {shark_speed}, Number of sharks: {num_sharks}, Treasures: {num_treasures}")

# --------------------- Game Setup ---------------------
import pygame
from player_design import Player
from treasure_design import Treasure
from shark_design import Shark
import random
import time

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pirate Treasure Game")
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)

# Sounds
background_sound = pygame.mixer.Sound("Background Music Treasure Hunt.mp3")
gamewin_sound = pygame.mixer.Sound("Gamewin Sound.mp3")
gameover_sound = pygame.mixer.Sound("Gameover Treasure Hunt.mp3")
lose_life_sound = pygame.mixer.Sound("life lost sound treasure hunt.mp3")

background_sound.play(-1)

# Load background
background_image = pygame.image.load("ocean background image.jpg")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Sprite groups
all_sprites = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
shark_group = pygame.sprite.Group()

# Create player
player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
player.speed_x = player_speed
player.speed_y = player_speed
all_sprites.add(player)

# Create treasures
for i in range(num_treasures):
    while True:
        x = random.randint(50, WINDOW_WIDTH - 50)
        y = random.randint(50, WINDOW_HEIGHT - 50)
        treasure = Treasure(x, y)
        if not pygame.sprite.spritecollideany(treasure, treasure_group):
            all_sprites.add(treasure)
            treasure_group.add(treasure)
            break

# --------------------- Game Variables ---------------------
running = True
gamewin = False
gameover = False
score = 0
sharks_spawned = False
shark_spawn_time = pygame.time.get_ticks() + 2000
last_shark_hit = None
last_hit_time = 0
HIT_COOLDOWN = 1000

# --------------------- Game Loop ---------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# --------------------- Shark Spawning---------------------------
# Loop until a valid position is found
# Pick random x position
# Pick random y position
# Create Shark  at this position
# Check if Shark is far enough from player horizontally
# Check if Shark is far enough from player vertically
# Check if Shark is not overlapping any treasure
# Check if Shark is not overlapping any other shark
# Add Shark to all sprites group
# Add Shark to shark group
# Exit loop once a valid position is found

    if not sharks_spawned and pygame.time.get_ticks() >= shark_spawn_time:
        # Shark 1
        while True:
            x1 = random.randint(50, WINDOW_WIDTH - 50)
            y1 = random.randint(50, WINDOW_HEIGHT - 50)
            shark1 = Shark(x1, y1, shark_speed, shark_speed)
            if (x1 < player.rect.centerx - 100 or x1 > player.rect.centerx + 100) and \
               (y1 < player.rect.centery - 100 or y1 > player.rect.centery + 100) and \
               not pygame.sprite.spritecollideany(shark1, treasure_group) and \
               not pygame.sprite.spritecollideany(shark1, shark_group):
                all_sprites.add(shark1)
                shark_group.add(shark1)
                break

        if num_sharks > 1:
            # Shark 2
            while True:
                x2 = random.randint(50, WINDOW_WIDTH - 50)
                y2 = random.randint(50, WINDOW_HEIGHT - 50)
                shark2 = Shark(x2, y2, shark_speed, shark_speed)
                if (x2 < player.rect.centerx - 100 or x2 > player.rect.centerx + 100) and \
                   (y2 < player.rect.centery - 100 or y2 > player.rect.centery + 100) and \
                   not pygame.sprite.spritecollideany(shark2, treasure_group) and \
                   not pygame.sprite.spritecollideany(shark2, shark_group):
                    all_sprites.add(shark2)
                    shark_group.add(shark2)
                    break

        if num_sharks > 2:
            # Shark 3
            while True:
                x3 = random.randint(50, WINDOW_WIDTH - 50)
                y3 = random.randint(50, WINDOW_HEIGHT - 50)
                shark3 = Shark(x3, y3, shark_speed, shark_speed)
                if (x3 < player.rect.centerx - 100 or x3 > player.rect.centerx + 100) and \
                   (y3 < player.rect.centery - 100 or y3 > player.rect.centery + 100) and \
                   not pygame.sprite.spritecollideany(shark3, treasure_group) and \
                   not pygame.sprite.spritecollideany(shark3, shark_group):
                    all_sprites.add(shark3)
                    shark_group.add(shark3)
                    break

        if num_sharks > 3:
            # Shark 4
            while True:
                x4 = random.randint(50, WINDOW_WIDTH - 50)
                y4 = random.randint(50, WINDOW_HEIGHT - 50)
                shark4 = Shark(x4, y4, shark_speed, shark_speed)
                if (x4 < player.rect.centerx - 100 or x4 > player.rect.centerx + 100) and \
                   (y4 < player.rect.centery - 100 or y4 > player.rect.centery + 100) and \
                   not pygame.sprite.spritecollideany(shark4, treasure_group) and \
                   not pygame.sprite.spritecollideany(shark4, shark_group):
                    all_sprites.add(shark4)
                    shark_group.add(shark4)
                    break

        if num_sharks > 4:
            # Shark 5
            while True:
                x5 = random.randint(50, WINDOW_WIDTH - 50)
                y5 = random.randint(50, WINDOW_HEIGHT - 50)
                shark5 = Shark(x5, y5, shark_speed, shark_speed)
                if(x5 < player.rect.centerx - 100 or x5 > player.rect.centerx + 100) and \
                   (y5 < player.rect.centery - 100 or y5 > player.rect.centery + 100) and \
                   not pygame.sprite.spritecollideany(shark5, treasure_group) and \
                   not pygame.sprite.spritecollideany(shark5, shark_group):
                    all_sprites.add(shark5)
                    shark_group.add(shark5)
                    break

        sharks_spawned = True

    # --------------------- Update ---------------------
    if not gamewin and not gameover:
        all_sprites.update()

        # Collect treasures
        treasures_collected = pygame.sprite.spritecollide(player, treasure_group, True)
        score += len(treasures_collected) * 10

        # Shark collision (cooldown)
        shark_hit = pygame.sprite.spritecollideany(player, shark_group)
        current_time = pygame.time.get_ticks()
        if shark_hit and (shark_hit != last_shark_hit or current_time - last_hit_time > HIT_COOLDOWN):
            lives -= 1
            last_shark_hit = shark_hit
            last_hit_time = current_time

            # Respawn player
            player.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

            # Push sharks away if too close
            for shark in shark_group:
                while shark.rect.centerx >= player.rect.centerx - 100 and shark.rect.centerx <= player.rect.centerx + 100 \
                  and shark.rect.centery >= player.rect.centery - 100 and shark.rect.centery <= player.rect.centery + 100:
                    shark.rect.centerx = random.randint(50, WINDOW_WIDTH - 50)
                    shark.rect.centery = random.randint(50, WINDOW_HEIGHT - 50)

            lose_life_sound.play()
            pygame.time.delay(500)
            if lives <=1:
                lose_life_sound.stop()
            if lives <= 0:
                gameover = True

        # Win
        if len(treasure_group) == 0 and not gamewin:
            gamewin = True

    # --------------------- Draw ---------------------
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, WHITE), (10, 50))
    boss_font = pygame.font.SysFont("Arial", 25, bold=True)
    screen.blit(boss_font.render("Boss: Group of Sharks", True, WHITE), (10, 80))

    # --------------------- End Screens ---------------------
    if gamewin:
        screen.fill("black")
        background_sound.stop()
        gamewin_sound.play()
        win_text = font.render("Congratulations! You collected all treasures!", True, WHITE)
        win_rect = win_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        screen.blit(win_text, win_rect)
        pygame.display.update()
        pygame.time.delay(5000)
        running = False

    if gameover:
        screen.fill("black")
        background_sound.stop()
        gameover_sound.play()
        lost_text = font.render("Game Over! You hit too many sharks!", True, WHITE)
        lost_rect = lost_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        screen.blit(lost_text, lost_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
