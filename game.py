import pygame
from pygame import RESIZABLE

import config
from snake import Snake
from food import Food
from input_handler import InputHandler
from renderer import Renderer

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SUPER Snake")

        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), RESIZABLE)
        self.clock = pygame.time.Clock()

        self.renderer = Renderer(self.screen)

        self.running = True
        self.paused = False
        self.game_over = False

        self.init_game_objects()

        self.input_handler = InputHandler(self.snake, self)

        self.move_delay = config.MOVE_DELAY
        self.time_since_move = 0

    def init_game_objects(self):
        start_x = config.COLUMNS // 2
        start_y = config.ROWS // 2

        self.snake = Snake(start_x, start_y, step=1, start_length=3, current_direction="RIGHT")

        self.food = Food(self.snake)
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game_tick(self):
        self.snake.update()

        if self.snake.collide_self():
            self.game_over = True
            return

        if self.snake.head() == self.food.pos:
            self.score += 1
            self.snake.grow()
            self.food.random_respawn(self.snake)

        hx, hy = self.snake.head()
        if not (0 <= hx < config.COLUMNS and 0 <= hy < config.ROWS):
            self.game_over = True

    def toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused

    def restart(self):
        self.paused = False
        self.game_over = False

        self.init_game_objects()

        self.input_handler.snake = self.snake
        self.input_handler.prev_keys = pygame.key.get_pressed()
        self.time_since_move = 0

    def quit(self):
        self.running = False

    def render(self):
        self.renderer.render(self.snake, self.food, self.score, self.paused, self.game_over)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()

            self.input_handler.input_process()

            dt = self.clock.tick(config.FPS)

            if not self.paused and not self.game_over:
                self.time_since_move += dt

                while self.time_since_move >= self.move_delay:
                    self.game_tick()
                    self.time_since_move -= self.move_delay

            self.render()
