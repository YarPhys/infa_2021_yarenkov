import pygame.surface  # Импортирование "под"экрана

import Ball
import Gun
import Target
import Constants

pygame.init()

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
total = 0
balls = []
targets = []
for i in range(Constants.num_targets):
    targets.append(Target(screen))

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

while not finished:
    screen.fill(Constants.WHITE)
    gun.draw()
    for b in balls:
        b.draw()
    for t in targets:
        t.draw()
    gun.move()
    pygame.display.update()

    clock.tick(Constants.FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                finished = True
            if event.key == pygame.K_w:
                gun.vy = 0.05
            if event.key == pygame.K_s:
                gun.vy = -0.05
            if event.key == pygame.K_d:
                gun.vx = 5
            if event.key == pygame.K_a:
                gun.vx = -5
            if event.key == pygame.K_0:
                Ball.kind_of_shells = 0
            if event.key == pygame.K_1:
                Ball.kind_of_shells = 1
            if event.key == pygame.K_2:
                Ball.kind_of_shells = 2
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.vx = 0
            if event.key == pygame.K_a:
                gun.vx = 0
            if event.key == pygame.K_w:
                gun.vy = 0
            if event.key == pygame.K_s:
                gun.vy = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color_to_shoot = gun.fire2_start()
            gun.color = color_to_shoot
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event, color_to_shoot)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.lived_for >= b.lifespan:
            balls.remove(b)
            continue
        for t in targets:
            if b.hit_test(t):
                total += t.cost
                balls.remove(b)
                targets.remove(t)
                targets.append(Target(screen))
                break
    gun.power_up()

pygame.quit()
