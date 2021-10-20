import pygame as pg
from pygame.draw import circle
from random import randint
import pygame.freetype
import ctypes

pygame.init()

FPS = 60
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(1)
length = user32.GetSystemMetrics(0)
screen = pg.display.set_mode((length, width - 80))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN,  WHITE]

s = 0  # счетчик попаданий
f = []  # массив всех шариков
dt = 0
pg.font.init()
myfont = pg.freetype.SysFont('Courier New', 24)


def Creating_balls(f):
    """ Создаем шарик """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(25, 40)
    speed_x = randint(5, 8) * (-1) ** randint(0, 1)
    speed_y = randint(5, 8) * (-1) ** randint(0, 1)
    color = COLORS[randint(0, 6)]
    if dt % 45 == 0:
        circle(screen, color, (x, y), r)
        f = f.append([x, y, r, color, speed_x, speed_y])


def Move_balls(f):
    """ Сдвигаем шарики и изменяем счет """
    for i in range(len(f)):
        if f[i][0] < f[i][2] or f[i][0] > length - f[i][2]:
            f[i][4] = -f[i][4]
        if f[i][1] < f[i][2] or f[i][1] > width - f[i][2]:
            f[i][5] = -f[i][5]
        f[i][0] = f[i][0] + f[i][4]
        f[i][1] = f[i][1] + f[i][5]
        circle(screen, f[i][3], (f[i][0], f[i][1]), f[i][2])
    myfont.render_to(screen, (50, 50), 'Score: ' + str(s), 'yellow')


def Removing_and_Scoring(f, event, s):
    """ убиваем шарик и увеличиваем счет """
    for i in range(len(f)):
        if (event.pos[0] - f[i][0]) ** 2 + (event.pos[1] - f[i][1]) ** 2 <= (f[i][2]) ** 2:
            f[i] = [0, 0, 0, 0, 0, 0]
            s += 1
    return s


clock = pg.time.Clock()
finish = True

while finish:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            s = Removing_and_Scoring(f, event, s)

    #  Здесь мы создаём шарик, передвигаем все шарики на экране и обновляем экран
    Creating_balls(f)
    dt += 1
    Move_balls(f)
    pg.display.update()
    screen.fill(BLACK)

pygame.quit()
