import random
import pygame
import Constants


class Target:
    def __init__(self, surface: pygame.Surface):
        """ Конструктор класса Target"""
        self.live = 1
        self.cost = 1
        self.surface = surface
        self.x = random.randint(round(0.6 * Constants.WIDTH), round(0.9 * Constants.WIDTH))
        self.y = random.randint(round(0.1 * Constants.HEIGHT), round(0.9 * Constants.HEIGHT))
        self.r = random.randint(10, 15)
        self.color = Constants.RED
        self.color_square = Constants.BLUE

    def draw(self):
        """Отрисовка целей"""
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)
