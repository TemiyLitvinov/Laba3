import pygame
import config


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(config.FONT_NAME, 20)

    def cell_pixel(self, cell):
        x, y = cell
        return x * config.SIZE_CELL, y * config.SIZE_CELL

    def draw_grid(self):
        for x in range(0, config.WIDTH, config.SIZE_CELL):
            pygame.draw.line(self.screen, config.GRID_COLOR, (x, 0), (x, config.WIDTH))
        for y in range(0, config.HEIGHT, config.SIZE_CELL):
            pygame.draw.line(self.screen, config.GRID_COLOR, (0, y), (config.HEIGHT, y))

