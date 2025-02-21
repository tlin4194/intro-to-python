import pygame
import random
import os
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30


class Game:
    game_speed = 5  # Class variable to control the speed of all objects

    def __init__(self):
        # Initialize screen and clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Obstacle Dodging Game")
        self.clock = pygame.time.Clock()

        # Load and resize images
        self.background_image = pygame.transform.scale(
            pygame.image.load("background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.heart_image = pygame.transform.scale(
            pygame.image.load("heart.png"), (30, 30)
        )
        self.coin_image = pygame.transform.scale(
            pygame.image.load("coin.png"), (20, 20)
        )
        self.cookie_image = pygame.transform.scale(
            pygame.image.load("cookie.png"), (25, 25)
        )

        # Initialize game elements
        self.background = Background(self.background_image)
        self.character = Character(self.screen)
        self.enemies = []
        self.obstacles = []
        self.coins = []
        self.cookies = []
        self.lives = 3
        self.start_time = pygame.time.get_ticks()
        self.high_score = self.load_high_score()
        self.coins_collected = 0
        self.running = True
        self.attack_mode = False
        self.attack_start_time = None

    def load_high_score(self):
        high_score_file = "high_score.txt"
        if os.path.exists(high_score_file):
            with open(high_score_file, "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        score = pygame.time.get_ticks() - self.start_time
        if score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(int(score)))

    def spawn_enemy(self):
        if random.randint(1, 100) < 3:
            self.enemies.append(Enemy(self.screen))

    def spawn_obstacle(self):
        if random.randint(1, 100) < 3:
            self.obstacles.append(Obstacle(self.screen))

    def spawn_coin_cluster(self):
        if random.randint(1, 100) < 2:
            for i in range(random.randint(3, 5)):
                self.coins.append(Coin(self.screen, x_offset=i * 30))

    def spawn_cookie(self):
        if random.randint(1, 100) < 1:
            self.cookies.append(Cookie(self.screen))

    def handle_collisions(self):
        character_rect = self.character.get_rect()

        for enemy in self.enemies[:]:
            if character_rect.colliderect(enemy.get_rect()):
                if self.attack_mode:  # Attack mode prevents losing a life
                    self.enemies.remove(enemy)
                else:
                    self.lives -= 1
                    self.character.show_hit_effect()
                    self.enemies.remove(enemy)

        for obstacle in self.obstacles[:]:
            if character_rect.colliderect(obstacle.get_rect()):
                self.lives -= 1
                self.character.show_hit_effect()
                self.obstacles.remove(obstacle)

        for coin in self.coins[:]:
            if character_rect.colliderect(coin.get_rect()):
                self.coins_collected += 1
                self.coins.remove(coin)

        for cookie in self.cookies[:]:
            if character_rect.colliderect(cookie.get_rect()) and self.lives < 3:
                self.lives += 1
                self.cookies.remove(cookie)

    def run(self):
        while self.running:
            self.handle_events()
            self.update_game_state()
            self.render_game()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.activate_attack_mode()

    def activate_attack_mode(self):
        self.attack_mode = True
        self.attack_start_time = pygame.time.get_ticks()

    def update_game_state(self):
        self.character.move()
        self.spawn_enemy()
        self.spawn_obstacle()
        self.spawn_coin_cluster()
        self.spawn_cookie()

        # Handle collisions and attack mode timing
        self.handle_collisions()
        self.update_attack_mode()

        # End game if lives are depleted
        if self.lives <= 0:
            self.running = False
            self.save_high_score()

    def update_attack_mode(self):
        # End attack mode after 2 seconds
        if self.attack_mode and (pygame.time.get_ticks() - self.attack_start_time) > 2000:
            self.attack_mode = False

    def render_game(self):
        self.screen.fill((0, 0, 0))
        self.background.scroll(self.screen)

        # Draw and move objects
        self.character.draw(self.attack_mode)
        for enemy in self.enemies:
            enemy.move_and_draw()
        for obstacle in self.obstacles:
            obstacle.move_and_draw()
        for coin in self.coins:
            coin.move_and_draw()
        for cookie in self.cookies:
            cookie.move_and_draw()

        # Display UI elements
        self.update_score_display()
        self.update_lives_display()
        self.update_high_score_display()
        pygame.display.flip()

    def update_score_display(self):
        font = pygame.font.Font(None, 36)
        score = pygame.time.get_ticks() - self.start_time
        score_text = font.render(
            f"Score: {score // 1000} s", True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50))

    def update_lives_display(self):
        for i in range(self.lives):
            self.screen.blit(self.heart_image, (20 + i * 40, 60))

    def update_high_score_display(self):
        font = pygame.font.Font(None, 36)
        high_score_text = font.render(
            f"High Score: {self.high_score // 1000} s", True, (255, 255, 255))
        self.screen.blit(high_score_text, (SCREEN_WIDTH - 150, 20))


class Background:
    def __init__(self, image):
        self.image = image
        self.x = 0

    def scroll(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + SCREEN_WIDTH, 0))
        self.x -= Game.game_speed
        if self.x <= -SCREEN_WIDTH:
            self.x = 0


class Character:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load("character.png"), (50, 50))
        self.x = 50
        self.y = SCREEN_HEIGHT // 2 - 25
        self.speed = 5
        self.hit_effect = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.image.get_height():
            self.y += self.speed

    def draw(self, attack_mode):
        if attack_mode:
            pygame.draw.rect(self.screen, (0, 0, 255), self.get_rect(), 3)
        elif self.hit_effect:
            pygame.draw.rect(self.screen, (255, 0, 0), self.get_rect(), 3)
        self.screen.blit(self.image, (self.x, self.y))

    def show_hit_effect(self):
        self.hit_effect = True

    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))


class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load("enemy.png"), (40, 40))
        self.rect = self.image.get_rect(
            topleft=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - 40)))

    def move_and_draw(self):
        self.rect.x -= Game.game_speed
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


class Obstacle:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load("obstacle.png"), (60, 60))
        self.rect = self.image.get_rect(
            topleft=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - 60)))

    def move_and_draw(self):
        self.rect.x -= Game.game_speed
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


class Coin:
    def __init__(self, screen, x_offset=0):
        self.screen = screen
        self.image = pygame.transform.scale
