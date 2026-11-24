import pygame
from settings import WIDTH, HEIGHT


class Player:

    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - 25,
            HEIGHT - 75,
            50,
            50
        )
        self.speed = 6
        self.health = 3

    def move(self, dx):
        self.rect.x += dx * self.speed

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)


class Bullet:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 5, y - 15, 10, 20)
        self.speed = 9

    def update(self):
        self.rect.y -= self.speed


class Monster:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 45, 45)
        self.speed_x = 2
        self.speed_y = 18

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed_x *= -1
            self.rect.y += self.speed_y


class GameModel:

    def __init__(self):
        self.player = Player()

        self.bullets = []

        self.monsters = [
            Monster(100, 100),
            Monster(250, 100),
            Monster(400, 100),
            Monster(550, 100),
            Monster(700, 100)
        ]

        self.score = 0
        self.status = "PLAYING"

    def shoot(self):
        if self.status == "PLAYING":
            bullet_x = self.player.rect.centerx
            bullet_y = self.player.rect.top

            self.bullets.append(
                Bullet(bullet_x, bullet_y)
            )

    def update(self):

        if self.status != "PLAYING":
            return

        for bullet in self.bullets:
            bullet.update()

        self.bullets = [
            bullet for bullet in self.bullets
            if bullet.rect.bottom > 0
        ]

        for monster in self.monsters:
            monster.update()

            if monster.rect.bottom >= self.player.rect.top:
                self.player.health -= 1
                monster.rect.y = 70

                if self.player.health <= 0:
                    self.status = "GAME OVER"

        for bullet in self.bullets[:]:
            for monster in self.monsters[:]:

                if bullet.rect.colliderect(monster.rect):
                    self.bullets.remove(bullet)
                    self.monsters.remove(monster)
                    self.score += 10
                    break

        if not self.monsters and self.status == "PLAYING":
            self.status = "YOU WIN"