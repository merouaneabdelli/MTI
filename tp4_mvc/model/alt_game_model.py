import random
from model.game_board import GameBoard
from model.entities import Monster

class CatchGameModel(GameBoard):
    
    def player_shoot(self):
        
        if self.status == "RUNNING":
            self.player.speed = 12.0

    def update(self):
        self.events.clear()
        if self.status != "RUNNING":
            return

        self.spawn_timer += 1
        if self.spawn_timer >= 35:
            self.spawn_timer = 0
            self.monsters.append(Monster(x=random.randint(0, self.width - 45), y=0, speed=4.0))

        for item in self.monsters[:]:
            item.update()
            if item.collides_with(self.player):
                
                self.score += 20
                self.monsters.remove(item)
                self.events.append("shoot")
            elif item.y > self.height:
                self.player.health -= 20
                self.monsters.remove(item)

        if self.player.health <= 0:
            self.player.health = 0
            self.status = "GAME_OVER"