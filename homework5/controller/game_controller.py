import pygame

class GameController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_theme = "default"

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.model.player_shoot()
                elif event.key == pygame.K_p:
                    self.model.toggle_pause()
                elif event.key == pygame.K_r and self.model.status in ("GAME_OVER", "WIN"):
                    self.model.reset()
                elif event.key == pygame.K_n and self.model.status == "WIN":
                    self.model.clone_level()
                elif event.key == pygame.K_t:
                    
                    if self.current_theme == "default":
                        self.view.change_theme("assets/theme_retro")
                        self.current_theme = "retro"
                    else:
                        self.view.change_theme("assets/theme_default")
                        self.current_theme = "default"

        
        keys = pygame.key.get_pressed()
        if self.model.status == "RUNNING":
            if keys[pygame.K_LEFT]:
                self.model.player.move_left()
            if keys[pygame.K_RIGHT]:
                self.model.player.move_right(self.model.width)
            if keys[pygame.K_UP]:
                self.model.player.move_up(0)
            if keys[pygame.K_DOWN]:
                self.model.player.move_down(self.model.height)    

    def run(self):
        while self.running:
            self.handle_input()
            self.model.update()
            self.view.render()
            self.clock.tick(60)
        pygame.quit()