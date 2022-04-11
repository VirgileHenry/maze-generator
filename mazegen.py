#coding:utf-8

from tkinter import *
import math
import random

cellNbr = int(input("Number of cells ? "))
cellSize = int(input("Size of a cell ? "))
wallSize = int(input("Size of a wall ? "))
mazeSize = cellNbr * (cellSize + wallSize) + wallSize

main = Tk()
main.title("Maze generator")
main.resizable(width=False, height=False)
canvas = Canvas(main, width=mazeSize, height=mazeSize, background="#ffffff")
canvas.place(x=0, y=0)


main.minsize(mazeSize, mazeSize)
runner = [math.trunc(cellNbr /2), math.trunc(cellNbr /2)]
maze = []
path = []
travel = []
run = True
for i in range(cellNbr):
   maze.append([])
   for j in range(cellNbr):
      maze[i].append([False, 'close', 'close', 'close', 'close'])


def convert(x):
   if x == 0:
      x = [0, -1]
   elif x == 1:
      x = [1, 0]
   elif x == 2:
      x = [0, 1]
   elif x == 3:
      x = [-1, 0]
   return x


def drawMaze():
   for i in range(cellNbr):
      for j in range(cellNbr):
         if maze[i][j][1] == 'close':
            canvas.create_rectangle( wallSize+i*(wallSize+cellSize),wallSize+j*(wallSize+cellSize),wallSize+cellSize+i*(wallSize+cellSize),j*(wallSize+cellSize),fill="white")
         if maze[i][j][2] == 'close':
            canvas.create_rectangle( wallSize+cellSize+i*(wallSize+cellSize),wallSize+j*(wallSize+cellSize),2*wallSize+cellSize+i*(wallSize+cellSize),wallSize+cellSize+j*(wallSize+cellSize),fill="white")
         if maze[i][j][3] == 'close':
            canvas.create_rectangle( wallSize+i*(wallSize+cellSize),cellSize+wallSize+j*(wallSize+cellSize),wallSize+cellSize+i*(wallSize+cellSize),2*wallSize+cellSize+j*(wallSize+cellSize),fill="white")
         if maze[i][j][4] == 'close':
            canvas.create_rectangle( wallSize+i*(wallSize+cellSize),wallSize+j*(wallSize+cellSize),i*(wallSize+cellSize),cellSize+wallSize+j*(wallSize+cellSize),fill="white")
   for i in range(cellNbr +1):
      for j in range(cellNbr +1):
         canvas.create_rectangle( i * (cellSize + wallSize), j * (cellSize + wallSize), wallSize + i * (cellSize + wallSize), wallSize + j * (cellSize + wallSize), fill="white")



def update_runner():
   global runner
   global run
   valid_cells = []
   if runner[1] > 0 and maze[runner[0]][runner[1]-1][0] == False:
      valid_cells.append(0)
   if runner[0]+1 < cellNbr and maze[runner[0]+1][runner[1]][0] == False:
      valid_cells.append(1)
   if runner[1]+1 < cellNbr and maze[runner[0]][runner[1]+1][0] == False:
      valid_cells.append(2)
   if runner[0] > 0 and maze[runner[0]-1][runner[1]][0] == False:
      valid_cells.append(3)
   
   if len(valid_cells) != 0:
      move = valid_cells[random.randint(1, len(valid_cells)) - 1]
      if move == 0:
         maze[runner[0]][runner[1]][1] = 'open'
         maze[runner[0]][runner[1]-1][3] = 'open'
      elif move == 1:
         maze[runner[0]][runner[1]][2] = 'open'
         maze[runner[0]+1][runner[1]][4] = 'open'
      elif move == 2:
         maze[runner[0]][runner[1]][3] = 'open'
         maze[runner[0]][runner[1]+1][1] = 'open'
      elif move == 3:
         maze[runner[0]][runner[1]][4] = 'open'
         maze[runner[0]-1][runner[1]][2] = 'open'
      move = convert(move)
      runner[0] = runner[0] + move[0]
      runner[1] = runner[1] + move[1]
      maze[runner[0]][runner[1]][0] = True
      travel.append([runner[0], runner[1]])
   else:
      travel.reverse()
      travel.pop(0)
      if len(travel) != 0:
         runner[0] = travel[0][0]
         runner[1] = travel[0][1]
      else:
         run = False
      travel.reverse()
   canvas.delete('runner')

def build_maze():
   while run == True:
      update_runner()
   drawMaze()


build_maze()
main.mainloop()