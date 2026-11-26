class Entity:
    
    def __init__(self, x: float, y: float, width: int, height: int, speed: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def collides_with(self, other: "Entity") -> bool:
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )


class Player(Entity):
    def __init__(self, x: float, y: float, width: int = 50, height: int = 50, speed: float = 6.0):
        super().__init__(x, y, width, height, speed)
        self.health = 100

    def move_left(self):
        self.x = max(0, self.x - self.speed)

    def move_right(self, board_width: int):
        self.x = min(board_width - self.width, self.x + self.speed)

    def move_up(self, min_y: float = 0):
        self.y = max(min_y, self.y - self.speed)

    def move_down(self, board_height: int):
        self.y = min(board_height - self.height, self.y + self.speed)
        
    def shoot(self) -> "Bullet":
        bullet_x = self.x + self.width / 2 - 4
        bullet_y = self.y - 15
        return Bullet(bullet_x, bullet_y)    


class Monster(Entity):
    def __init__(self, x: float, y: float, width: int = 45, height: int = 45, speed: float = 2.0):
        super().__init__(x, y, width, height, speed)

    def update(self):
        self.y += self.speed


class Bullet(Entity):
    def __init__(self, x: float, y: float, width: int = 8, height: int = 16, speed: float = 9.0):
        super().__init__(x, y, width, height, speed)

    def update(self):
        self.y -= self.speed


import math


class Monster(Entity):
    def __init__(self, x: float, y: float, width: int = 45, height: int = 45, speed: float = 2.0):
        super().__init__(x, y, width, height, speed)

    def update(self, player: "Entity | None" = None):
        if player is not None:
            self.follow(player)
        else:
            self.y += self.speed

    def follow(self, target: "Entity"):
        dx = (target.x + target.width / 2) - (self.x + self.width / 2)
        dy = (target.y + target.height / 2) - (self.y + self.height / 2)
        distance = math.hypot(dx, dy)

        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed