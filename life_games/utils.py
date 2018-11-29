import pygame as pg


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
