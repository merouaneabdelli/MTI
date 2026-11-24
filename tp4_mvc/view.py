import pygame

from settings import (
    WIDTH, HEIGHT, WHITE, BLACK, BLUE, RED, YELLOW, DARK,
    PLAYER_IMAGE, MONSTER_IMAGE, BULLET_IMAGE,
    BACKGROUND_IMAGE, SHOOT_SOUND
)


class GameView:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("TP4 - Jeu MVC")

        self.font = pygame.font.Font(None, 32)
        self.big_font = pygame.font.Font(None, 72)

        self.player_image = self.load_image(PLAYER_IMAGE, (50, 50))
        self.monster_image = self.load_image(MONSTER_IMAGE, (45, 45))
        self.bullet_image = self.load_image(BULLET_IMAGE, (10, 20))

        self.background_image = self.load_image(
            BACKGROUND_IMAGE, (WIDTH, HEIGHT)
        )

        self.shoot_sound = None

        try:
            self.shoot_sound = pygame.mixer.Sound(str(SHOOT_SOUND))
        except (pygame.error, FileNotFoundError):
            pass

    def load_image(self, path, size):
        try:
            image = pygame.image.load(str(path)).convert_alpha()
            return pygame.transform.scale(image, size)

        except (pygame.error, FileNotFoundError):
            return None

    def play_shoot_sound(self):
        if self.shoot_sound:
            self.shoot_sound.play()

    def draw_object(self, image, rect, color):

        if image:
            self.screen.blit(image, rect)

        else:
            pygame.draw.rect(
                self.screen, color, rect, border_radius=8
            )

    def render(self, model):

        if self.background_image:
            self.screen.blit(self.background_image, (100, 100))

        else:
            self.screen.fill(DARK)

        self.draw_object(
            self.player_image, model.player.rect, BLUE
        )

        for monster in model.monsters:
            self.draw_object(
                self.monster_image, monster.rect, RED
            )

        for bullet in model.bullets:
            self.draw_object(
                self.bullet_image, bullet.rect, YELLOW
            )

        pygame.draw.rect(
            self.screen, BLACK, (0, 0, WIDTH, 45)
        )

        score_text = self.font.render(
            f"Score: {model.score}", True, WHITE
        )

        health_text = self.font.render(
            f"Health: {model.player.health}", True, WHITE
        )

        status_text = self.font.render(
            f"Status: {model.status}", True, WHITE
        )

        self.screen.blit(score_text, (15, 12))
        self.screen.blit(health_text, (250, 12))
        self.screen.blit(status_text, (500, 12))

        if model.status != "PLAYING":

            message = self.big_font.render(
                model.status, True, YELLOW
            )

            message_rect = message.get_rect(
                center=(WIDTH // 2, HEIGHT // 2)
            )

            self.screen.blit(message, message_rect)

        pygame.display.flip()