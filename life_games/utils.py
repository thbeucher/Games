import pygame as pg


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
