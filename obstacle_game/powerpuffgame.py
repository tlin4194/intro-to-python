import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions and FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30


class Game:
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
        self.score = 0
        self.high_score = self.load_high_score()
        self.coins_collected = 0
        self.running = True

    def load_high_score(self):
        high_score_file = "high_score.txt"
        if os.path.exists(high_score_file):
            with open(high_score_file, "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(int(self.score)))

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
                # Attack enemy if space is pressed
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.enemies.remove(enemy)
                else:
                    self.lives -= 1
                    self.enemies.remove(enemy)

        for obstacle in self.obstacles[:]:
            if character_rect.colliderect(obstacle.get_rect()):
                self.lives -= 1
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
        while self.running:  # game loop

            # exits game if you close the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.background.scroll(self.screen)

            # Update game elements
            self.character.move()
            self.spawn_enemy()
            self.spawn_obstacle()
            self.spawn_coin_cluster()
            self.spawn_cookie()

            # Draw game elements
            self.character.draw()
            for enemy in self.enemies:
                enemy.move_and_draw()
            for obstacle in self.obstacles:
                obstacle.move_and_draw()
            for coin in self.coins:
                coin.move_and_draw()
            for cookie in self.cookies:
                cookie.move_and_draw()

            # Handle collisions
            self.handle_collisions()

            # Display UI elements (score, lives, high score)
            self.update_score_display()
            self.update_lives_display()
            self.update_high_score_display()
            self.update_coins_display()

            # Check for game over
            if self.lives <= 0:
                self.running = False

            pygame.display.flip()
            self.clock.tick(FPS)

        self.save_high_score()

    def update_score_display(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50))

    def update_lives_display(self):
        for i in range(self.lives):
            self.screen.blit(self.heart_image, (20 + i * 40, 60))

    def update_high_score_display(self):
        font = pygame.font.Font(None, 36)
        high_score_text = font.render(
            f"High Score: {int(self.high_score)}", True, (255, 255, 255)
        )
        self.screen.blit(high_score_text, (SCREEN_WIDTH - 200, 20))

    def update_coins_display(self):
        font = pygame.font.Font(None, 36)
        coin_text = font.render(
            f"Coins: {int(self.coins_collected)}", True, (255, 255, 255)
        )
        self.screen.blit(coin_text, (SCREEN_WIDTH - 150, 60))


class Background:
    def __init__(self, image):
        self.image = image
        self.x = 0
        self.speed = 4

    def scroll(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + SCREEN_WIDTH, 0))
        self.x -= self.speed
        if self.x <= -SCREEN_WIDTH:
            self.x = 0


class Character:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load("character.png"), (50, 50)
        )
        self.x = 50
        self.y = SCREEN_HEIGHT // 2 - 25
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.image.get_height():
            self.y += self.speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))


class GameObject:
    def __init__(self, screen, image_file, image_x, image_y):
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load(image_file), (image_x, image_y)
        )
        self.rect = self.image.get_rect(
            topleft=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - 40))
        )
        self.speed = 4

    def move_and_draw(self):
        self.rect.x -= self.speed
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


class Enemy(GameObject):
    def __init__(self, screen):
        super().__init__(screen, "enemy.png", 40, 40)


class Obstacle(GameObject):
    # def __init__(self, screen):
    #     self.screen = screen
    #     self.image = pygame.transform.scale(
    #         pygame.image.load("obstacle.png"), (60, 60))
    #     self.rect = self.image.get_rect(
    #         topleft=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - 60)))
    #     self.speed = 4

    def __init__(self, screen):
        super().__init__(screen, "obstacle.png", 60, 60)


class Coin(GameObject):
    # def __init__(self, screen, x_offset=0):
    #     self.screen = screen
    #     self.image = pygame.transform.scale(
    #         pygame.image.load("coin.png"), (20, 20))
    #     self.rect = self.image.get_rect(
    #         topleft=(SCREEN_WIDTH + x_offset, random.randint(0, SCREEN_HEIGHT - 20)))
    #     self.speed = 4

    def __init__(self, screen, x_offset=0):
        super().__init__(screen, "coin.png", 20, 20)
        self.rect = self.image.get_rect(
            topleft=(SCREEN_WIDTH + x_offset, random.randint(0, SCREEN_HEIGHT - 20))
        )


class Cookie(GameObject):
    # def __init__(self, screen):
    #     self.screen = screen
    #     self.image = pygame.transform.scale(
    #         pygame.image.load("cookie.png"), (25, 25))
    #     self.rect = self.image.get_rect(
    #         topleft=(SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - 25)))
    #     self.speed = 4

    def __init__(self, screen):
        super().__init__(screen, "cookie.png", 25, 25)


# Main entry point
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
