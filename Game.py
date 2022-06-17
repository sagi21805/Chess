from re import I
import pygame
import numpy as np

class Game():

  def __init__(self, Size_x :int, Size_y: int, NumOfRows: int):
    self.Size_x = Size_x
    self.Size_y = Size_y
    self.NumOfRows = NumOfRows
    self.running = True
    self.surface = pygame.display.set_mode((self.Size_x, self.Size_y))
    self.color = ("black")
    self.surface.fill("white")
    
    for r in range(0, self.NumOfRows):
      if r % 2 == 0:
        for i in range(0, self.NumOfRows):
          if i % 2 == 0 or i == 0:
            pygame.draw.rect(self.surface, "white" , pygame.Rect((i * (self.Size_x / self.NumOfRows)), (r * (self.Size_y / self.NumOfRows)),((i + 1) * (self.Size_x / self.NumOfRows)), (i  +1 * (self.Size_y / self.NumOfRows))))
          else:
            pygame.draw.rect(self.surface, (162, 216, 99), pygame.Rect((i * (self.Size_x / self.NumOfRows)), (r * (self.Size_y / self.NumOfRows)),((i + 1) * (self.Size_x / self.NumOfRows)), (i  +1 * (self.Size_y / self.NumOfRows))))
      else:
        for i in range(0, self.NumOfRows):
          if i % 2 == 0 or i == 0:
            pygame.draw.rect(self.surface, (162, 216, 99), pygame.Rect((i * (self.Size_x / self.NumOfRows)), (r * (self.Size_y / self.NumOfRows)),((i + 1) * (self.Size_x / self.NumOfRows)), (i  +1 * (self.Size_y / self.NumOfRows))))
          else:
            pygame.draw.rect(self.surface, "white" , pygame.Rect((i * (self.Size_x / self.NumOfRows)), (r * (self.Size_y / self.NumOfRows)),((i + 1) * (self.Size_x / self.NumOfRows)), (i  +1 * (self.Size_y / self.NumOfRows))))
    
    WhitePawn = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White Pawn.png")
    WhiteKnight = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White Knight.png")
    WhiteRook = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White Rook.png")
    WhiteBishop = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White Bishop.png")
    WhiteKing = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White King.png")
    WhiteQueen = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\White Queen.png")
    BlackPawn = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black Pawn.png")
    BlackKnight = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black Knight.png")
    BlackRook = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black Rook.png")
    BlackBishop = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black Bishop.png")
    BlackKing = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black King.png")
    BlackQueen = pygame.image.load("C:\\vscodeprojects\\python\\Chess\\Chess-1\\images\\Black Queen.png")
    
    self.Cells: list[list[Cell]] = []
    for n in range(0, self.NumOfRows):
      row: list[Cell] = []
      for i in range(0, self.NumOfRows):
        cell = Cell(n, i)
        print([n, i])
        match i:
          case 0:
            match n:
              case 0 | 7:
                self.surface.blit(BlackRook, (((n * self.Size_x / self.NumOfRows) + 15), (i * (self.Size_y) / self.NumOfRows)))
                cell.type = "black rook"
              case 1 | 6:
                self.surface.blit(BlackKnight, (((n * self.Size_x / self.NumOfRows) + 20), (i * (self.Size_y) / self.NumOfRows) - 5))
                cell.type = "black knight"
              case 2 | 5:
                self.surface.blit(BlackBishop, (((n * self.Size_x / self.NumOfRows) + 5), (i * (self.Size_y) / self.NumOfRows) + 5))
                cell.type = "black bishop"
              case 3:
                self.surface.blit(BlackQueen, (((n * self.Size_x / self.NumOfRows) + 10), (i * (self.Size_y) / self.NumOfRows)))
                cell.type = "black queen"
              case 4:
                self.surface.blit(BlackKing, (((n * self.Size_x / self.NumOfRows) + 10), (i * (self.Size_y) / self.NumOfRows)))
                cell.type = "black king"
          case 1:
            self.surface.blit(BlackPawn, (((n * self.Size_x / self.NumOfRows) + 15), (i * (self.Size_y) / self.NumOfRows)))
            cell.type = "black pawn"
          case 6:
            self.surface.blit(WhitePawn, (((n * self.Size_x / self.NumOfRows) + 15), (i * (self.Size_y) / self.NumOfRows)))
            cell.type = "white pawn"
          case 7:
            match n:
              case 0 | 7:
                self.surface.blit(WhiteRook, (((n * self.Size_x / self.NumOfRows) + 10), (i * (self.Size_y) / self.NumOfRows) - 5))
                cell.type = "white rook"
              case 1 | 6:
                self.surface.blit(WhiteKnight, (((n * self.Size_x / self.NumOfRows) + 10), (i * (self.Size_y) / self.NumOfRows) + 3))
                cell.type = "white knight"
              case 2 | 5:
                self.surface.blit(WhiteBishop, (((n * self.Size_x / self.NumOfRows) + 15), (i * (self.Size_y) / self.NumOfRows) + 5))
                cell.type = "white bishop"
              case 3:
                self.surface.blit(WhiteQueen, (((n * self.Size_x / self.NumOfRows) + 5), (i * (self.Size_y) / self.NumOfRows)))
                cell.type = "white queen"
              case 4:
                self.surface.blit(WhiteKing, (((n * self.Size_x / self.NumOfRows) + 5), (i * (self.Size_y) / self.NumOfRows)))
                cell.type = "white king"
        row.append(cell)
      self.Cells.append(row)
      
    pygame.display.update()
    
  def ChangeUnits(self) -> list: 
    pos = list(pygame.mouse.get_pos())
    x = int(np.floor(int(pos[0]) / (self.Size_x / self.NumOfRows)))
    y = int(np.floor(int(pos[1]) / (self.Size_y / self.NumOfRows)))
    cords = []
    cords.append(x)
    cords.append(y)
    return cords
      
  def start(self):
      while self.running:        
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
              print(self.Cells[self.ChangeUnits()[0]][self.ChangeUnits()[1]].type)

            
            if event.type == pygame.QUIT:
              self.running = False   
            
class Cell():
  
  def __init__(self, position_x: int, position_y: int):
    self.position_x = position_x
    self.position_y = position_y
    self.type = "empty"

    
CHESS = Game(800, 700, 8)
CHESS.start()