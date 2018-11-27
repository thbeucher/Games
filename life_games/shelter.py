import math
import utils as u
import numpy as np
import pygame as pg
import tensorflow as tf

COLORS = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
          'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}

class Circle:
  def __init__(self, init_pos, size=10, color=COLORS['black'], num_out=2):
    self.size = size
    self.color = color
    self.surface = pg.display.get_surface()
    self.rect = pg.draw.circle(self.surface, color, init_pos, size)

  def draw(self):
    pos = self.rect.x + self.size, self.rect.y + self.size
    pg.draw.circle(self.surface, self.color, pos, self.size)

  def move(self, vector):
    angle, speed = vector
    rad_angle = angle * math.pi / 180
    dx = speed * math.cos(rad_angle)
    dy = speed * math.sin(rad_angle)
    self.rect = self.rect.move(dx, dy)
    u.check_borders([self.rect])
