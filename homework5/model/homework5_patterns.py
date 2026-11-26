"""Homework 5 design patterns: Factory Method, Builder and Prototype."""
from copy import deepcopy

from model.entities import Zombie, Dragon, Robot



# 1) FACTORY METHOD: subclasses choose which concrete monster to create.
class MonsterFactory:
    def create_monster(self, monster_type, x, y):
        monster_type = monster_type.lower()
        if monster_type == "zombie":
            return Zombie(x, y)
        if monster_type == "dragon":
            return Dragon(x, y)
        if monster_type == "robot":
            return Robot(x, y)
        raise ValueError(f"Unknown monster type: {monster_type}")


class ZombieFactory(MonsterFactory):
    def create_monster(self, monster_type="zombie", x=0, y=0):
        return super().create_monster("zombie", x, y)


class DragonFactory(MonsterFactory):
    def create_monster(self, monster_type="dragon", x=0, y=0):
        return super().create_monster("dragon", x, y)


class RobotFactory(MonsterFactory):
    def create_monster(self, monster_type="robot", x=0, y=0):
        return super().create_monster("robot", x, y)



# 2) BUILDER: assemble level settings step by step.
class GameLevel:
    def __init__(self, name="Level 1", spawn_interval=50, monster_types=None, target_score=100):
        self.name = name
        self.spawn_interval = spawn_interval
        self.monster_types = list(monster_types or ["zombie"])
        self.target_score = target_score

    def clone(self):
        """3) PROTOTYPE: return an independent copy of this level."""
        return deepcopy(self)



class GameLevelBuilder:
    def __init__(self):
        self.reset()



    def reset(self):
        self._level = GameLevel()
        return self



    def set_name(self, name):
        self._level.name = name
        return self



    def set_spawn_interval(self, interval):
        self._level.spawn_interval = max(1, int(interval))
        return self



    def add_monster_type(self, monster_type):
        monster_type = monster_type.lower()
        if monster_type in ("zombie", "dragon", "robot") and monster_type not in self._level.monster_types:
            self._level.monster_types.append(monster_type)
        return self



    def set_target_score(self, score):
        self._level.target_score = max(10, int(score))
        return self



    def build(self):
        result = self._level.clone()
        self.reset()
        return result



    @staticmethod
    def build_default_level():
        return (GameLevelBuilder()
                .set_name("Level 1")
                .set_spawn_interval(50)
                .add_monster_type("zombie")
                .add_monster_type("dragon")
                .add_monster_type("robot")
                .set_target_score(100)
                .build())
