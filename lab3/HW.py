import pygame as pg

pg.init()
screen = pg.display.set_mode((455, 300))

pg.draw.polygon(screen, (200, 200, 255), ((0, 0), (0, 150), (455, 150), (455, 0)))
pg.draw.polygon(screen, (0, 255, 20), ((0, 150), (0, 300), (455, 300), (455, 150)))

def house(x, y, a):
    pg.draw.rect(screen, (101, 67, 32), (x, y, 2*a, a))
    pg.draw.rect(screen, (100, 200, 255), (x + 3*a/4, y + 3*a/8, a/2, a/4))
    pg.draw.polygon(screen, (255, 0, 0), ((x, y), (x + 2*a, y), (x + a, y - 3*a/4)))

def cloud(x, y ,a):
    b = 1
    for i in range(4):
        pg.draw.circle(screen, (255, 255, 255), (x + b, y), a)
        pg.draw.circle(screen, (0, 0, 0), (x + b, y), a, 1)
        b += a/2
    pg.draw.circle(screen, (255, 255, 255), (x + a/2, y - a/2), a)
    pg.draw.circle(screen, (0, 0, 0), (x + a / 2, y - a / 2), a, 1)
    pg.draw.circle(screen, (255, 255, 255), (x + a, y - a/2), a)
    pg.draw.circle(screen, (0, 0, 0), (x + a, y - a/2), a, 1)

def tree(x, y, a):
    pg.draw.rect(screen, (191, 67, 38), (x - a/2, y, 3*a/2, 10*a))
    pg.draw.circle(screen, (1, 50, 25), (x + 3*a, y - 5*a), 6*a)
    pg.draw.circle(screen, (1, 50, 25), (x - 3*a, y - 5*a), 6*a)
    pg.draw.circle(screen, (1, 50, 25), (x + a, y - 7*a), 6*a)
    pg.draw.circle(screen, (1, 50, 25), (x, y - 12*a), 6*a)
    pg.draw.circle(screen, (1, 50, 25), (x + 4*a, y - a), 6*a)
    pg.draw.circle(screen, (1, 50, 25), (x - 4*a, y - a), 6*a)

house(50, 160, 90)
house(300, 156, 40)
cloud(100, 70, 20)
cloud(360, 90, 20)
cloud(240, 110, 10)
tree(260, 230, 5)
tree(420, 180, 3)
pg.draw.circle(screen, (255, 100, 150), (40, 40), 35) 

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
