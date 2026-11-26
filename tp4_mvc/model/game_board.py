import random
from model.entities import Player, Monster, Bullet

class GameBoard:
    
    def __init__(self, width: int = 800, height: int = 600 , win_scor = 100):
        self.width = width
        self.height = height
        self.win_scor = win_scor
        self.reset()
        if self.player.health <= 0:
            self.player.health = 0
            self.status == "GAME_OVER"
        elif self.score >= self.win_scor:
            self.status == "WIN"
          
    def reset(self):
        self.player = Player(x=self.width // 2 - 25, y=self.height - 80)
        self.monsters: list[Monster] = []
        self.bullets: list[Bullet] = []
        self.score = 0
        self.status = "RUNNING"  
        self.spawn_timer = 0
        self.events: list[str] = []  

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
        if self.spawn_timer >= 50:
            self.spawn_timer = 0
            spawn_x = random.randint(0, self.width - 45)
            self.monsters.append(Monster(x=spawn_x, y=0))

        
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

  