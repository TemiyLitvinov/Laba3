import pygame
from snake import Snake


class InputHandler:
    def __init__(self, snake: Snake, game):
        self.snake = snake
        self.game = game

        self.prev_keys = pygame.key.get_pressed()

    def input_process(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.snake.set_direction("UP")
        elif keys[pygame.K_DOWN]:
            self.snake.set_direction("DOWN")
        elif keys[pygame.K_LEFT]:
            self.snake.set_direction("LEFT")
        elif keys[pygame.K_RIGHT]:
            self.snake.set_direction("RIGHT")

        self._edge_trigger(keys, pygame.K_p, self.game.toggle_pause)
        self._edge_trigger(keys, pygame.K_r, self.game.restart)
        self._edge_trigger(keys, pygame.K_q, self.game.quit)
        self.prev_keys = keys

    def _edge_trigger(self, keys, key, callback):
        if keys[key] and not self.prev_keys[key]:
            callback()
