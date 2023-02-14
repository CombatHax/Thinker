import pygame as pg
pg.init()

def draw_circle(screen, x, y, r, c, cam_offset):
    pg.draw.circle(screen, c, (x + cam_offset[0], y + cam_offset[1]), r)
def draw_rect(screen, x, y, w, h, c, cam_offset):
    pg.draw.rect(screen, c, (x, y, w, h))