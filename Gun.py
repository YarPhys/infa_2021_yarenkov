import math
from random import choice

import pygame

from Ball import Ball
from main import screen
import Constants

gun_x = Constants.WIDTH // 40
gun_y = round(0.75 * Constants.HEIGHT)
gun_vx = 0
gun_vy = 0


class Gun:
    def __init__(self, surface: pygame.Surface, x=gun_x, y=gun_y, vx=gun_vx, vy=gun_vy):
        """ Конструктор класса Gun"""
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = Constants.GREY
        self.max_length = 100
        self.min_length = 10
        self.width = 10

    def fire2_start(self):
        """Начало арт-обстрела целей"""
        self.f2_on = 1
        # self.shell = int
        return choice(Constants.colors)

    def fire2_end(self, event, color):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.surface)
        new_ball.color = color
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return new_ball.color

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши"""
        if event:
            self.an = math.atan2((event.pos[1] - gun_y), (event.pos[0] - gun_x))
        if self.f2_on is False:
            self.color = Constants.GREY

    def draw(self):
        """Отрисовка шкалы силы выстрела"""
        length = self.min_length + self.max_length * (self.f2_power - 10) / 90
        width = self.width
        x1, y1 = length * math.cos(self.an), length * math.sin(self.an)
        x2, y2 = width * math.sin(self.an), width * math.cos(self.an)
        pygame.draw.polygon(screen, self.color, ((gun_x, gun_y), (gun_x + x1, gun_y + y1),
                                                 (gun_x + x1 + x2, gun_y + y1 - y2), (gun_x + x2, gun_y - y2)))
        # FIXED!

    def power_up(self):
        """Увеличение силы выстрела"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
        else:
            self.color = Constants.GREY

    def move(self):
        """Движение пушки в пространстве"""
        self.x += self.vx
        self.y += self.vy
        pass
