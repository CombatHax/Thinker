import pygame as pg
pg.init()
from drawers import draw_circle, draw_rect

class Gate:
    inputs = 2
    outputs = 1
    text = "Gate"
    def __init__(self, pos):
        self.pos = pos
    def draw(self, surf, offset):
        draw_rect(surf, self.pos[0], self.pos[1] - 10, 40, 40 * (max(self.outputs, self.inputs) + .5), (255, 255, 255), offset)
