import pygame
from collections import deque


class Snake:
    def __init__(self, x, y, speed, start_length = 3, current_direction = 'RIGHT'):
        self.x = x
        self.y = y
        self.speed = speed
        self.body = deque()
        self.start_length = start_length
        self.start_direction = current_direction
        self.next_direction = current_direction
        self.grow_pending = 0

    def set_direction(self, new_direction):
        opposite_directions = {'UP' : 'DOWN', 'DOWN' : 'UP', 'LEFT' : 'RIGHT', 'RIGHT' : 'LEFT'}

        if new_direction == opposite_directions[new_direction]:
            return
        self.next_direction = new_direction
