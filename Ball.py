from random import choice
import pygame
from Gun import gun_x, gun_y
import Constants


class Ball:
    def __init__(self, surface: pygame.Surface, x=gun_x, y=gun_y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.shell = int
        self.surface = surface
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(Constants.colors)
        self.live = 30
        self.lifespan = 100  # Время жизни шарика
        self.lived_for = 0

    def move(self):
        """ Перемещаем мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей
        на мяч, и стен по краям окна (размер окна равен размеру экрана пользователя).
        """
        # FIXED!
        self.lived_for += 1
        self.x += self.vx
        self.y += self.vy
        self.vy += Constants.dvy
        self.vy += -self.vy * Constants.resistance_k
        self.vx += -self.vx * Constants.resistance_k
        if (0 < self.x < Constants.WIDTH) is False:
            self.vx = -self.vx
        if (0 < self.y < Constants.HEIGHT) is False:
            self.vy = -self.vy * Constants.bounce_k

    def kind_of_shells(self):
        """
        Зоология снарядов
        """
        if self.shell == 0:
            self.color = Constants.colors[0]
            self.lifespan = 100
        if self.shell == 1:
            self.color = Constants.colors[1]
            self.lifespan = 30
        if self.shell == 2:
            self.color = Constants.colors[2]
            self.lifespan = 15000
            self.vx /= 23
            self.vy /= 2
        if self.shell == 3:
            self.color = Constants.colors[3]
            self.lifespan = 130
        if self.shell == 4:
            self.color = Constants.colors[4]
            self.lifespan = 15

    def draw(self):
        """Отрисовка снаряда"""
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r, self.shell())

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.r + obj.r) ** 2 >= (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2
