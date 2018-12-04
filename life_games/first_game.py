import utils as u
import pygame as pg
from shelter import Circle, Rectangle
# import tensorflow.contrib.eager as tfe


# tfe.enable_eager_execution()


colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
          'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}

pg.init()
win_size = (400, 400)

screen = pg.display.set_mode(win_size)
screen.fill(colors['white'])
c = Circle((50, 50))

food1 = Circle((100, 100))
target_rect = Rectangle((food1.rect.x, food1.rect.y, 20, 20), color=colors['green'])
moving_rect = Rectangle((150, 150, 20, 20), color=colors['red'])
subject_to_predation = [c, food1]
other_objs = [target_rect, moving_rect]

# ar = pg.surfarray.array2d(screen)
# print(ar)
# print(ar.shape)
# u.matprint(ar[39:61:1, 39:61:1])

obj_to_move = moving_rect
while 1:
  for e in pg.event.get():
    if e.type == pg.KEYDOWN:
      if e.key == pg.K_ESCAPE:
        pg.quit()
        quit()
      if e.key == pg.K_UP:
        obj_to_move.move((270, 5), list_obj_for_colision=list_objs)
      if e.key == pg.K_DOWN:
        obj_to_move.move((90, 5), list_obj_for_colision=list_objs)
      if e.key == pg.K_LEFT:
        obj_to_move.move((180, 5), list_obj_for_colision=list_objs)
      if e.key == pg.K_RIGHT:
        obj_to_move.move((0, 5), list_obj_for_colision=list_objs)
      if e.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
        print(u.box_l2_loss(moving_rect, target_rect))
    if e.type == pg.QUIT:
      pg.quit()
      quit()

  screen.fill(colors['white'])
  u.predation(subject_to_predation)
  list_objs = u.remove_corps(subject_to_predation)
  u.draw_obj(subject_to_predation + other_objs)
  pg.display.flip()
