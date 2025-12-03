import pygame


class Game:
    pygame.init()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()