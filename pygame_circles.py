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

    r2 = randint(25, 40)
    r3 = randint(25, 40)
    r4 = randint(25, 40)
    r4 = randint(25, 40)
    color = COLORS[randint(0, 6)]
    pygame.draw.circle(screen, color, (x, y), r)
    color = COLORS[randint(0, 6)]
    pygame.draw.circle(screen, color, (x1, y1), r1)
    color = COLORS[randint(0, 6)]
    pygame.draw.circle(screen, color, (x2, y2), r2)
    color = COLORS[randint(0, 6)]
    pygame.draw.circle(screen, color, (x3, y3), r3)
    color = COLORS[randint(0, 6)]
    pygame.draw.circle(screen, color, (x4, y4), r4)
    
def move_circle():
    '''двигает круги '''
    global x, x1, x2, x3, x4, y, y1, y2, y3, y4, r, r1, r2, r3, r4
    dt = 0.1
    for i in range(int(clock.tick(FPS)/dt)):
        x += 20*dt
        y += 15*dt
        screen.fill(BLACK)
    
def click(event):
    '''находит координаты появившегося очередного круга'''
    print(x, y, r)
    print(x1, y1, r1)
    print(x2, y2, r2)
    print(x3, y3, r3)
    print(x4, y4, r4)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Вы убили ", counter, " невинных кружОЧКОВ D-:")
            #print("Из ", points, " возможных X-D")
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print('Click!')
            click(pygame.MOUSEBUTTONDOWN)
            if ((event.pos[0] - x)**2 + (event.pos[1] - y)**2 )**0.5 <= r:
                counter += 1
                #screen.fill(BLACK)
                #pygame.draw.polygon(screen, MAGENTA, ((1100, 0), (1100, 800), (1200, 800), (1200, 900), 6)
            if ((event.pos[0] - x1)**2 + (event.pos[1] - y1)**2 )**0.5 <= r1:
                counter += 1
            if ((event.pos[0] - x2)**2 + (event.pos[1] - y2)**2 )**0.5 <= r2:
                counter += 1                
            if ((event.pos[0] - x3)**2 + (event.pos[1] - y3)**2 )**0.5 <= r3:
                counter += 1    
            if ((event.pos[0] - x4)**2 + (event.pos[1] - y4)**2 )**0.5 <= r4:
                counter += 1   
                
    new_circle()
    pygame.display.update()
    screen.fill(BLACK)
    points += 5
    
    move_circle()

pygame.quit()

