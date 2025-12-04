import pygame
from collections import deque


class Snake:
    def __init__(self, x, y, step, start_length = 3, current_direction = 'RIGHT'):
        self.x = x
        self.y = y
        self.step = step
        self.body = deque()
        self.start_length = start_length
        self.current_direction = current_direction
        self.next_direction = current_direction
        self.grow_pending = 0

    def set_direction(self, new_direction):
        opposite_directions = {'UP' : 'DOWN', 'DOWN' : 'UP', 'LEFT' : 'RIGHT', 'RIGHT' : 'LEFT'}

        if new_direction == opposite_directions[new_direction]:
            return
        self.next_direction = new_direction

    def update(self):
        self.current_direction = self.next_direction
        head_x, head_y = self.body[0]
        if self.current_direction == 'UP':
            head_y += self.step
        elif self.current_direction == 'DOWN':
            head_y -= self.step
        elif self.current_direction == 'LEFT':
            head_x -= self.step
        elif self.current_direction == 'RIGHT':
            head_x += self.step

        new_head = (head_x, head_y)
        self.body.append(new_head)

        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount = 1):
        self.grow_pending += amount

    def head(self):
        return self.body[0]

    def collide_self(self):
        head = self.head()
        return head in list(self.body)[1:]

    def occupies(self, pos):
        return pos in self.body

    def current_length(self):
        return len(self.body)