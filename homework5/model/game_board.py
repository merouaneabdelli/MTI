import random
from model.entities import Player, Bullet
from model.homework5_patterns import MonsterFactory, GameLevelBuilder



class GameBoard:
    def __init__(self, width: int = 800, height: int = 600, win_scor: int = 100):
        self.width = width
        self.height = height
        self.factory = MonsterFactory()
        self.level = GameLevelBuilder.build_default_level()
        self.level_number = 1
        self.win_scor = self.level.target_score
        self.reset()



    def reset(self):
        self.player = Player(x=self.width // 2 - 25, y=self.height - 80)
        self.monsters = []
        self.bullets = []
        self.score = 0
        self.status = "RUNNING"
        self.spawn_timer = 0
        self.events = []
        self.level_name = self.level.name



    def clone_level(self):
        """Prototype: clone the current level, then tweak the clone for next level."""
        self.level = self.level.clone()
        level_number = getattr(self, "level_number", 1) + 1
        self.level_number = level_number
        self.level.name = f"Level {level_number}"
        self.level.spawn_interval = max(20, self.level.spawn_interval - 5)
        self.level.target_score += 50
        self.win_scor = self.level.target_score
        self.reset()
        self.level_name = self.level.name



    def toggle_pause(self):
        if self.status == "RUNNING":
            self.status = "PAUSED"
        elif self.status == "PAUSED":
            self.status = "RUNNING"



    def player_shoot(self):
        if self.status == "RUNNING":
            self.bullets.append(self.player.shoot())
            self.events.append("shoot")



    def update(self):
        self.events.clear()
        if self.status != "RUNNING":
            return

        self.spawn_timer += 1
        if self.spawn_timer >= self.level.spawn_interval:
            self.spawn_timer = 0
            spawn_x = random.randint(0, self.width - 45)
            monster_type = random.choice(self.level.monster_types)
            self.monsters.append(self.factory.create_monster(monster_type, spawn_x, 0))



        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y + bullet.height < 0:
                self.bullets.remove(bullet)

        for monster in self.monsters[:]:
            monster.update(self.player)
            if monster.collides_with(self.player):
                self.player.health -= 25
                self.monsters.remove(monster)
                self.events.append("hit")
            elif monster.y > self.height:
                self.player.health -= 10
                self.monsters.remove(monster)

        for bullet in self.bullets[:]:
            for monster in self.monsters[:]:
                if bullet.collides_with(monster):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if monster in self.monsters:
                        self.monsters.remove(monster)
                    self.score += 10
                    self.events.append("hit")
                    break

        if self.player.health <= 0:
            self.player.health = 0
            self.status = "GAME_OVER"
        elif self.score >= self.win_scor:
            self.status = "WIN"
