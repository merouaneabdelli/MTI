import os
import pygame


class ResourceManager:
    

    IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

    def __init__(self, theme_path: str):
        self.theme_path = theme_path
        self.images: dict[str, pygame.Surface] = {}
        self.sounds: dict[str, pygame.mixer.Sound | None] = {}
        self.load_resources()

    def _find_image_file(self, subfolder: str, base_name: str) -> str | None:
        folder = os.path.join(self.theme_path, subfolder)
        for ext in self.IMAGE_EXTENSIONS:
            candidate = os.path.join(folder, f"{base_name}{ext}")
            if os.path.isfile(candidate):
                return candidate
        return None

    def _load_image(
        self,
        subfolder: str,
        base_name: str,
        size: tuple[int, int],
        fallback_color: tuple[int, int, int],
    ) -> pygame.Surface:
        found_path = self._find_image_file(subfolder, base_name)
        if found_path:
            try:
                img = pygame.image.load(found_path)
                if pygame.display.get_surface() is not None:
                    img = img.convert_alpha()
                return pygame.transform.smoothscale(img, size)
            except pygame.error as exc:
                print(f"[ResourceManager] فشل تحميل '{found_path}': {exc}")
        else:
            print(
                f"[ResourceManager] لم يتم العثور على '{base_name}.*' في "
                f"'{os.path.join(self.theme_path, subfolder)}' — سيتم استخدام اللون البديل."
            )

        surface = pygame.Surface(size)
        surface.fill(fallback_color)
        return surface

    def _load_sound(self, filename: str) -> pygame.mixer.Sound | None:
        path = os.path.join(self.theme_path, "sounds", filename)
        if os.path.isfile(path) and pygame.mixer.get_init() is not None:
            try:
                return pygame.mixer.Sound(path)
            except pygame.error as exc:
                print(f"[ResourceManager] فشل تحميل الصوت '{path}': {exc}")
        return None

    def load_resources(self) -> None:
        self.images["player"] = self._load_image("player", "player", (50, 50), (0, 200, 255))
        self.images["monster"] = self._load_image("monsters", "monster", (45, 45), (220, 50, 50))
        self.images["bullet"] = self._load_image("bullets", "bullet", (8, 16), (255, 230, 0))
        self.images["background"] = self._load_image("backgrounds", "bg", (800, 600), (18, 20, 35))

        self.sounds["shoot"] = self._load_sound("shoot.wav")
        self.sounds["hit"] = self._load_sound("hit.wav")