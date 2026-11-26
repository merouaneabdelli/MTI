import pygame
from view.resource_manager import ResourceManager


class GameView:
    

    def __init__(self, model, theme_path: str = "assets/theme_default"):
        if not pygame.get_init():
            pygame.init()
        if pygame.display.get_surface() is None:
            pygame.display.init()

        self.model = model
        self.panel_height = 50
        self.screen = pygame.display.set_mode(
            (self.model.width, self.model.height + self.panel_height)
        )
        pygame.display.set_caption("لعبة OOP - معمارية MVC")
        self.font = pygame.font.SysFont("Arial", 22, bold=True)
        self.theme_path = theme_path
        self.resources = ResourceManager(theme_path)
        self._scaled_bg: pygame.Surface | None = None
        self._refresh_scaled_background()

    def _refresh_scaled_background(self) -> None:
        bg = self.resources.images.get("background")
        if bg is not None:
            target_size = (self.model.width, self.model.height)
            if bg.get_size() != target_size:
                self._scaled_bg = pygame.transform.smoothscale(bg, target_size)
            else:
                self._scaled_bg = bg

    def change_theme(self, new_theme_path: str) -> None:
        
        self.theme_path = new_theme_path
        self.resources = ResourceManager(new_theme_path)
        self._refresh_scaled_background()

    def render(self) -> None:
        
        for event in getattr(self.model, "events", []):
            sound = self.resources.sounds.get(event)
            if sound:
                sound.play()

    
        pygame.draw.rect(
            self.screen, (30, 30, 45), (0, 0, self.model.width, self.panel_height)
        )
        info_text = (
            f"Score: {self.model.score}   |   "
            f"Health: {self.model.player.health}%   |   "
            f"Status: {self.model.status}"
        )
        text_surface = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (20, 12))

        
        offset_y = self.panel_height
        if self._scaled_bg is not None:
            self.screen.blit(self._scaled_bg, (0, offset_y))

        p = self.model.player
        self.screen.blit(self.resources.images["player"], (p.x, p.y + offset_y))

        for m in self.model.monsters:
            self.screen.blit(self.resources.images["monster"], (m.x, m.y + offset_y))

        for b in self.model.bullets:
            self.screen.blit(self.resources.images["bullet"], (b.x, b.y + offset_y))
           

        
        if self.model.status == "GAME_OVER":
            over_surf = self.font.render(
                "GAME OVER - Press R to Restart", True, (255, 80, 80)
            )
            rect = over_surf.get_rect(
                center=(self.model.width // 2, offset_y + self.model.height // 2)
            )
            self.screen.blit(over_surf, rect)
        elif self.model.status == "WIN":
            win_surf = self.font.render(
                "YOU WIN! - Press R to Play Again", True, (80, 255, 120)
            )
            rect = win_surf.get_rect(
                center=(self.model.width // 2, offset_y + self.model.height // 2)
            )
            self.screen.blit(win_surf, rect)

        pygame.display.flip()