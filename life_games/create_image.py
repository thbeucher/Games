import argparse
import pygame as pg


def create_circle(size, circle_color, background_color, filename):
  # margin = int(0.1 * size)
  margin = 0
  screen = pg.display.set_mode((2 * size + margin, 2 * size + margin))
  screen.fill(background_color)
  x = screen.get_width() // 2
  y = screen.get_height() // 2
  pg.draw.circle(screen, circle_color, (x, y), size)
  pg.image.save(screen, filename)


def create_cell(genome):
  colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
            'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}
  if genome == '00':
    screen = pg.display.set_mode((20, 20))
    screen.fill(colors['black'])
    pg.image.save(screen, 'images/' + genome + '.png')
  elif genome == '01':
    screen = pg.display.set_mode((40, 20))
    screen.fill(colors['white'])
    pg.draw.rect(screen, colors['black'], (0, 0, 20, 20))
    pg.draw.polygon(screen, colors['black'], [(20, 0), (20, 20), (40, 10)])
    pg.image.save(screen, 'images/' + genome + '.png')
  elif genome == '10':
    screen = pg.display.set_mode((60, 20))
    screen.fill(colors['white'])
    pg.draw.polygon(screen, colors['black'], [(20, 0), (40, 0), (40, 20), (20, 20)])
    pg.draw.polygon(screen, colors['black'], [(0, 10), (20, 0), (20, 20)])
    pg.draw.polygon(screen, colors['black'], [(40, 0), (40, 20), (60, 10)])
    pg.image.save(screen, 'images/' + genome + '.png')
  else:
    screen = pg.display.set_mode((60, 40))
    screen.fill(colors['white'])
    pg.draw.polygon(screen, colors['black'], [(20, 0), (40, 0), (40, 20), (20, 20)])
    pg.draw.polygon(screen, colors['black'], [(0, 10), (20, 0), (20, 20)])
    pg.draw.polygon(screen, colors['black'], [(40, 0), (40, 20), (60, 10)])
    pg.draw.polygon(screen, colors['black'], [(20, 20), (40, 20), (30, 40)])
    pg.image.save(screen, 'images/' + genome + '.png')


def create_triangle(colors):
  screen = pg.display.set_mode((20, 20))
  screen.fill(colors['white'])
  # pg.draw.polygon(screen, colors['black'], [(0, 10), (20, 0), (20, 20)])
  pg.draw.polygon(screen, colors['black'], [(0, 0), (0, 20), (20, 10)])
  pg.image.save(screen, 'images/triangle.png')


if __name__ == '__main__':
  colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'darkBlue': (0,0,128),
            'white': (255,255,255), 'black': (0,0,0), 'pink': (255,200,200)}


  # create_circle(30, colors['black'], colors['white'], 'images/black_circle_30.png')
  # create_triangle(colors)
  create_cell('11')
