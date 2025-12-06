import pygame
import config
from snake import Snake
from food import Food
from input_handler import InputHandler
from renderer import Renderer


class Game:
    def __init__(self, screen):
        pygame.init()
        pygame.display.set_caption("SUPER Snake")

        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()

        self.renderer = Renderer(self.screen)

        self.running = True
        self.paused = False
        self.game_over = False

        self.init_game_objects()

        self.input_handler = InputHandler(self.snake, self)

    def init_game_objects(self):

        start_x = config.COLUMNS // 2
        start_y = config.ROWS // 2

        self.snake = Snake(start_x, start_y, 3, start_length=3, current_direction="RIGHT")

        self.food = Food(self.snake)

        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):

        if self.paused or self.game_over:
            return

        # обработка клавиш
        self.input_handler.input_process()

        self.snake.update()

        if self.snake.head() == self.food.pos:
            self.score += 1
            self.snake.grow()
            self.food.random_respawn(self.snake)

    def toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused

    def restart(self):
        self.paused = False
        self.game_over = False
        self.init_game_objects()
        self.input_handler.snake = self.snake

    def quit(self):
        self.running = False

    def render(self):
        self.renderer.render(self.snake, self.food, self.score, self.paused, self.game_over)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(config.FPS)
