import pygame as pg
from math import floor, ceil

screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
pg.display.set_caption("I Have 3Ds")
cam_offset = [0, 0]
key_code = pg.key.key_code

def draw_circle(x, y, r, c):
    pg.draw.circle(screen, c, (x + cam_offset[0], y + cam_offset[1]), r)
def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

clock = pg.time.Clock()
hold = [0, 0]

while True:
    clock.tick(60)
    screen.fill((50, 50, 50))
    draw_circle(15, 15, 10, 1)
    for x in range(floor(-cam_offset[0] / 40) * 40, screen.get_size()[0] - cam_offset[0] + 40, 40):
        for y in range(floor(-cam_offset[1] / 40) * 40, screen.get_size()[1] - cam_offset[1] + 40, 40):
            draw_circle(x, y, 3, (40, 40, 40))
    keys = pg.key.get_pressed()
    '''
    if keys[key_code('w')]:
        cam_offset[1] += 5
    if keys[key_code('s')]:
        cam_offset[1] -= 5
    if keys[key_code('a')]:
        cam_offset[0] += 5
    if keys[key_code('d')]:
        cam_offset[0] -= 5
    '''
    mouse = [pg.mouse.get_pos(), pg.mouse.get_pressed()]
    if mouse[1][0]:
        if hold == None:
            hold = mouse
        else:
            cam_offset[0] += mouse[0][0] - hold[0]
            cam_offset[1] += mouse[0][1] - hold[1]
        hold = mouse[0]
    else:
        hold = None
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    pg.display.flip()