import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("Супер змейка", 20)

    def cell_pixel(self, cell):
        x, y = cell
        return x * 40, y * 40

    def draw_grid(self):
        for x in range(0, 1200, 40):
            pygame.draw.line(self.screen, (30, 30, 30), (x, 0), (x, 1200))
        for y in range(0, 800, 40):
            pygame.draw.line(self.screen, (30, 30, 30), (0, y), (800, y))

