import pygame
from snake import Snake
from game import Game


class InputHandler:
    def __init__(self, snake : Snake, game : Game):
        self.snake = snake
        self.game = game
        pygame.init()

    def input_proccess(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snake.set_direction("UP")
        elif keys[pygame.K_DOWN]:
            self.snake.set_direction("DOWN")
        elif keys[pygame.K_LEFT]:
            self.snake.set_direction("LEFT")
        elif keys[pygame.K_RIGHT]:
            self.snake.set_direction("RIGHT")