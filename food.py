import random
from snake import Snake


class Food:
    def __init__(self, snake : Snake):
        self.pos = (0, 0)
        self.respawn = snake

    def random_respawn(self, snake : Snake):
        x = random.randint(0, 30)
        y = random.randint(0, 20)
        if not snake.occupies((x, y)):
            self.pos = (x, y)
            return