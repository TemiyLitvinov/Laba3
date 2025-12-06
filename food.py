import random
import config
from snake import Snake


class Food:
    def __init__(self, snake: Snake):
        self.pos = None
        self.random_respawn(snake)

    def random_respawn(self, snake: Snake):
        while True:
            x = random.randint(0, config.COLUMNS - 1)
            y = random.randint(0, config.ROWS - 1)

            if not snake.occupies((x, y)):
                self.pos = (x, y)
                return
