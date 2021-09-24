

import pygame


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.circle(screen, (255, 255, 0), (200, 200), 150)
pygame.draw.circle(screen, (255, 0, 0), (150, 150), 40)
pygame.draw.circle(screen, (0, 0, 0), (150, 150), 20)
pygame.draw.circle(screen, (255, 0, 0), (250, 150), 30)
pygame.draw.circle(screen, (0, 0, 0), (250, 150), 10)
pygame.draw.rect(screen, (0, 0, 0), (100, 250, 200, 40))

pygame.draw.polygon(screen, (0, 0, 0), [(110,55), (100,75), (180,135), (190,125)])
pygame.draw.polygon(screen, (0, 0, 0), [(210,145), (200,130), (260,55), (270,70)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
