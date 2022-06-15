import pygame
import numpy as np

class Game():

  def __init__(self, Size_x :int, Size_y: int, NumOfRowsX, NumOfRowsY: int):
    self.Size_x = Size_x
    self.Size_y = Size_y
    self.NumOfRowsX = NumOfRowsX
    self.NumOfRowsY = NumOfRowsY
    self.running = True
    self.surface = pygame.display.set_mode((self.Size_x, self.Size_y))
    self.color = ("black")
    self.surface.fill("white")
    
    for r in range(0, self.NumOfRowsX):
      for i in range(0, self.NumOfRowsY):
        if i % 2 == 0 or i == 0:
          pygame.draw.rect(self.surface, "black", pygame.Rect((r * (self.Size_x / self.NumOfRowsX)), (i * (self.Size_y / self.NumOfRowsY)),((i + 1) * (self.Size_x / self.NumOfRowsX)), (i  +1 * (self.Size_y / self.NumOfRowsY))))
        else:
          pygame.draw.rect(self.surface, "white", pygame.Rect((r * (self.Size_x / self.NumOfRowsX)), (i * (self.Size_y / self.NumOfRowsY)),((i + 1) * (self.Size_x / self.NumOfRowsX)), (i  +1 * (self.Size_y / self.NumOfRowsY))))
      pygame.display.update()
    
    self.Cells: list[list[Cell]] = []
    for i in range(0, self.NumOfRowsY):
      row: list[Cell] = []
      for n in range(0, self.NumOfRowsX):
        cell = Cell(n, i)
        row.append(cell)
      self.Cells.append(row)
      
  def start(self):
      while self.running:        
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
              pass

            
            if event.type == pygame.QUIT:
              self.running = False   
            
class Cell():
  
  def __init__(self, position_x: int, position_y: int):
    self.position_x = position_x
    self.position_y = position_y
    self.O: bool = False
    self.X: bool = False
  
CHESS = Game(800, 700, 8, 8)
CHESS.start()