import pygame as pg
from drawing import Circle
import tensorflow.contrib.eager as tfe


tfe.enable_eager_execution()


colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
          'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}

pg.init()
win_size = (400, 400)

screen = pg.display.set_mode(win_size)
screen.fill(colors['white'])
c = Circle((100, 100))


while 1:
  for e in pg.event.get():
    if e.type == pg.KEYDOWN:
      if e.key == pg.K_ESCAPE:
        pg.quit()
        quit()
      if e.key == pg.K_UP:
        c.move((270, 5))
      if e.key == pg.K_DOWN:
        c.move((90, 5))
      if e.key == pg.K_LEFT:
        c.move((180, 5))
      if e.key == pg.K_RIGHT:
        c.move((0, 5))
    if e.type == pg.QUIT:
      pg.quit()
      quit()

  screen.fill(colors['white'])
  c.draw()
  pg.display.flip()
