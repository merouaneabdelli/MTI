import pygame

from model import GameModel
from view import GameView
from settings import FPS


class GameController:

    def __init__(self):
        self.model = GameModel()
        self.view = GameView()

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.model.shoot()
                    self.view.play_shoot_sound()

                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def handle_continuous_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.model.player.move(-1)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.model.player.move(1)

    def run(self):

        while self.running:

            self.handle_events()

            self.handle_continuous_input()

            self.model.update()

            self.view.render(self.model)

            self.clock.tick(FPS)


def main():

    pygame.init()

    controller = GameController()

    controller.run()

    pygame.quit()


if __name__ == "__main__":
    main()
