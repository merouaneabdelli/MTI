from pathlib import Path

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 255)
RED = (220, 60, 60)
YELLOW = (255, 220, 50)
DARK = (25, 30, 45)

ASSETS_DIR = Path(__file__).parent / "assets"

PLAYER_IMAGE = ASSETS_DIR / "player" / "player.png"
MONSTER_IMAGE = ASSETS_DIR / "monsters" / "monster.png"
BULLET_IMAGE = ASSETS_DIR / "bullets" / "bullet.png"
BACKGROUND_IMAGE = ASSETS_DIR / "backgrounds" / "background.png"
SHOOT_SOUND = ASSETS_DIR / "sounds" / "shoot.wav"