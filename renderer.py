import pygame
import config
from food import Food
from snake import Snake


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)  # временный шрифт

    def cell_pixel(self, cell):
        x, y = cell
        return x * config.SIZE_CELL, y * config.SIZE_CELL

    def draw_grid(self):
        for x in range(0, config.WIDTH, config.SIZE_CELL):
            pygame.draw.line(self.screen, config.GRID_COLOR, (x, 0), (x, config.HEIGHT))
        for y in range(0, config.HEIGHT, config.SIZE_CELL):
            pygame.draw.line(self.screen, config.GRID_COLOR, (0, y), (config.WIDTH, y))

    def draw_snake(self, snake: Snake):
        head = snake.body[0]
        for seg in snake.body:
            px, py = self.cell_pixel(seg)
            rect = pygame.Rect(px, py, config.SIZE_CELL, config.SIZE_CELL)

            if seg == head:
                pygame.draw.rect(self.screen, config.SNAKE_HEAD_COLOR, rect)
            else:
                pygame.draw.rect(self.screen, config.SNAKE_COLOR, rect)

    def draw_food(self, food: Food):
        px, py = self.cell_pixel(food.pos)
        center = (px + config.SIZE_CELL // 2, py + config.SIZE_CELL // 2)
        pygame.draw.circle(self.screen, config.FOOD_COLOR, center, config.SIZE_CELL // 2)

    def draw_score(self, score):
        txt = self.font.render(f"Score: {score}", True, config.TEXT_COLOR)
        self.screen.blit(txt, (10, 10))

    def draw_pause(self):
        txt = self.font.render("PAUSE", True, config.TEXT_COLOR)
        rect = txt.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
        self.screen.blit(txt, rect)

    def draw_game_over(self, score):
        txt = self.font.render("GAME OVER", True, config.TEXT_COLOR)
        rect = txt.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 - 50))
        self.screen.blit(txt, rect)

        sub = self.font.render(
            f"Score: {score} — Press R to restart or Q to quit",
            True,
            config.TEXT_COLOR
        )
        rect2 = sub.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + 20))
        self.screen.blit(sub, rect2)

    def render(self, snake, food, score, paused=False, game_over=False):
        self.screen.fill(config.BG_COLOR)

        self.draw_grid()
        self.draw_food(food)
        self.draw_snake(snake)
        self.draw_score(score)

        if paused:
            self.draw_pause()
        elif game_over:
            self.draw_game_over(score)