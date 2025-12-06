import pygame
from snake import Snake
from game import Game


class InputHandler:
    def __init__(self, snake : Snake, game : Game):
        pygame.init()
        self.snake = snake
        self.game = game

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

        if keys[pygame.K_p]:
            self.game.toggle_pause()

        if keys[pygame.K_r]:
            self.game.restart()

        if keys[pygame.K_q]:
            self.game.quit()