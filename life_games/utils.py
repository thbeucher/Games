import math
import numpy as np
import pygame as pg


def box_l2_loss(obj1, obj2):
  r1 = np.array([obj1.rect.x, obj1.rect.y, obj1.rect.width, obj1.rect.height])
  r2 = np.array([obj2.rect.x, obj2.rect.y, obj2.rect.width, obj2.rect.height])
  return np.linalg.norm(r1 - r2)


def move_from_vector(vector):
  angle, speed = vector
  rad_angle = angle * math.pi / 180
  dx = speed * math.cos(rad_angle)
  dy = speed * math.sin(rad_angle)
  return dx, dy


def draw_obj(list_obj):
  for obj in list_obj:
    obj.draw()


def remove_corps(list_obj):
  return [obj for obj in list_obj if obj.alive]


def predation(list_obj):
  names = [obj.name for obj in list_obj]
  for obj in list_obj:
    idx_prey = names.index(obj.prey) if obj.prey in names else -1
    if obj.prey != -1 and obj.prey != list_obj[idx_prey].prey:
      obj.grow()
      obj.prey = -1
      list_obj[idx_prey].eated()


def check_borders(obj_list):
  width, height = pg.display.get_surface().get_size()
  for el in obj_list:
    if el.x < 0:
      el.x = 0
    if el.y < 0:
      el.y = 0
    if el.x > height - 20:
      el.x = height - 20
    if el.y > width - 20:
      el.y = width - 20


def matprint(mat, fmt="g"):
  col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
  for x in mat:
    for i, y in enumerate(x):
      print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
    print("")
