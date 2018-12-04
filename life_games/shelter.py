import math
import utils as u
import numpy as np
import pygame as pg
from uuid import uuid4
# import tensorflow as tf

COLORS = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
          'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}


class Circle:
  def __init__(self, init_pos, size=10, color=COLORS['black'], eated_in=3, growth=1):
    self.name = str(uuid4())
    self.prey = -1
    self.alive = True
    self.size = size
    self.color = color
    self.growth = growth
    self.loose_size = int(size/eated_in) + 1
    self.surface = pg.display.get_surface()
    self.rect = pg.draw.circle(self.surface, color, init_pos, size)

  def draw(self):
    pos = self.rect.x + self.size, self.rect.y + self.size
    self.rect = pg.draw.circle(self.surface, self.color, pos, self.size)

  def move(self, vector, list_obj_for_colision=[]):
    dx, dy = u.move_from_vector(vector)
    new_rect = self.rect.move(dx, dy)
    other_obj = [obj for obj in list_obj_for_colision if obj is not self]
    idx_collide = new_rect.collidelist([obj.rect for obj in other_obj])
    if idx_collide == -1:
      self.rect = new_rect
      u.check_borders([self.rect])
    else:
      self.prey = other_obj[idx_collide].name

  def grow(self):
    self.rect = self.rect.inflate(self.growth, self.growth)
    self.size += self.growth

  def eated(self):
    self.rect = self.rect.inflate(-self.loose_size, -self.loose_size)
    self.size -= self.loose_size
    if self.size <= 0:
      self.alive = False


class Rectangle:
  def __init__(self, init_pos, color=COLORS['black'], width=1):
    self.color = color
    self.width = width
    self.surface = pg.display.get_surface()
    self.rect = pg.draw.rect(self.surface, color, init_pos, width)

  def draw(self):
    self.rect = pg.draw.rect(self.surface, self.color, self.rect, self.width)

  def move(self, vector, list_obj_for_colision=[]):
    dx, dy = u.move_from_vector(vector)
    self.rect = self.rect.move(dx, dy)
