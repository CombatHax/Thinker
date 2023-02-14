import pygame as pg
pg.init()
from math import floor, ceil
import time
from drawers import draw_circle, draw_rect
import Gate

screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
pg.display.set_caption("I Have 3Ds")
font = pg.font.SysFont("Comic Sans MS", 20)
cam_offset = [0, 0]
key_code = pg.key.key_code


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

clock = pg.time.Clock()
hold = [(0, 0)]
prev_sec = floor(time.time())
fps = font.render(str(floor(clock.get_fps())), False, (0, 0, 0))
stuff = []

while True:
    clock.tick()
    screen.fill((50, 50, 50))
    draw_circle(screen, 15, 15, 10, 1, cam_offset)
    for x in range(floor(-cam_offset[0] / 40) * 40, screen.get_size()[0] - cam_offset[0] + 40, 40):
        for y in range(floor(-cam_offset[1] / 40) * 40, screen.get_size()[1] - cam_offset[1] + 40, 40):
            draw_circle(screen, x, y, 3, (40, 40, 40), cam_offset)
    keys = pg.key.get_pressed()
    if floor(time.time()) != prev_sec:
        fps = font.render(str(floor(clock.get_fps())), False, (0, 0, 0))
        prev_sec = floor(time.time())
    screen.blit(fps, (0, 0))
    mouse = [pg.mouse.get_pos(), pg.mouse.get_pressed(), pg.mouse.get_pos()]
    if mouse[1][1]:
        if hold == None:
            hold = mouse
        else:
            cam_offset[0] += mouse[0][0] - hold[0]
            cam_offset[1] += mouse[0][1] - hold[1]
        hold = mouse[0]
    else:
        hold = None
    for thing in stuff:
        thing.draw(screen, cam_offset)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                where = (round((e.pos[0] - cam_offset[0]) / 40) * 40, round((e.pos[1] - cam_offset[1]) / 40) * 40)
                for thing in stuff:
                    if thing.pos == where:
                        break
                else:
                    stuff.append(Gate.Gate(where))
        
    pg.display.flip()