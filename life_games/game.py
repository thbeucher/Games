import sys
import math
import pygame as pg


def check_borders(obj_list):
  width, height = pg.display.get_surface().get_size()
  for i, el in enumerate(obj_list):
    if el.rect.x < 0:
      el.rect.x = 0
    if el.rect.y < 0:
      el.rect.y = 0
    if el.rect.x > height - 20:
      el.rect.x = height - 20
    if el.rect.y > width - 20:
      el.rect.y = width - 20


class Circle(pg.sprite.Sprite):
  def __init__(self, init_pos, filename='images/black_circle_10.png'):
    self.surface = pg.image.load(filename)
    self.rect = self.surface.get_rect()
    self.rect.x, self.rect.y = init_pos[0], init_pos[1]

  def move(self, vector, list_obj_for_colision):
    angle, z = vector
    rad_angle = angle * math.pi / 180
    dx = z * math.cos(rad_angle)
    dy = z * math.sin(rad_angle)
    new_rect = self.rect.move(dx, dy)
    if new_rect.collidelist(list_obj_for_colision) == -1:
      self.rect = new_rect


def launch_game(screen, colors):
  obj_list = [Circle((100, 100)), Circle((400, 400), filename='images/black_circle_30.png')]
  dirty_rects = [el.rect for el in obj_list]
  while 1:
    # 6 - draw the screen elements
    screen.fill(colors['white'])
    check_borders(obj_list)
    for i, el in enumerate(obj_list):
      dirty_rects[i] = screen.blit(el.surface, el.rect)
    # 7 - update the screen
    pg.display.update(dirty_rects)
    # 8 - loop through the events
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]: obj_list[0].move((270, 5), [dirty_rects[1]])
    if pressed[pg.K_DOWN]: obj_list[0].move((90, 5), [dirty_rects[1]])
    if pressed[pg.K_LEFT]: obj_list[0].move((180, 5), [dirty_rects[1]])
    if pressed[pg.K_RIGHT]: obj_list[0].move((360, 5), [dirty_rects[1]])

    for event in pg.event.get():
      # check if the event is the X button
      if event.type==pg.QUIT:
        # if it is quit the game
        pg.quit()
        exit(0)


if __name__ == '__main__':
  colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
            'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}

  pg.init()
  win_size = (800, 800)

  screen = pg.display.set_mode(win_size)

  launch_game(screen, colors)
