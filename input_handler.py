import pygame
from snake import Snake

keys = pygame.key.get_pressed()


class InputHandler:

    def __init__(self, snake : Snake):
        self.snake = snake
        pygame.init()

