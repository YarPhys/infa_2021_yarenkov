import pygame
from random import randint
pygame.init()


counter = 0  # Подсчёт количества очков
points = 0  # Подсчёт количества фигур, появившихся на экране за всё время игры 
FPS = 0.5  # Speed (level)
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

def new_circle():
    '''рисует новые круги '''
    global x, x1, x2, x3, x4, y, y1, y2, y3, y4, r, r1, r2, r3, r4
    x = randint(100, 1100)
    x1 = randint(100, 1100)
    x2 = randint(100, 1100)
    x3 = randint(100, 1100)
    x4 = randint(100, 1100)
    y = randint(100, 800)
    y1 = randint(100, 800)
    y2 = randint(100, 800)
    y3 = randint(100, 800)
    y4 = randint(100, 800)
    r = randint(25, 40)
    r1 = randint(25, 40)
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

