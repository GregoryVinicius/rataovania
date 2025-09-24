from game.core.game_object import GameObject

class Entity(GameObject):
    def __init__(self, position_x, position_y):
        super().__init__(name)
        self.x = position_x
        self.y = position_y
    