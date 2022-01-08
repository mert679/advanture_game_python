import random

EMPTY = 'e'
TREASURE = 't'
MONSTER = 'm'
VENOM = "v"
SWORD = 's'
POTION ='p'

whatToAddInGrid = (TREASURE, TREASURE, TREASURE, MONSTER, MONSTER, MONSTER, SWORD, SWORD, POTION, POTION,VENOM,VENOM,VENOM)


NROWS_IN_GRID = 6
NCOLS_IN_GRID = 8

grid = []

for r in range(0, NROWS_IN_GRID): #0-5
  aRow = []
  for c in range(0, NCOLS_IN_GRID):#0-7
    aRow.append(EMPTY)  
  grid.append(aRow)


def findEmptyCell(aGrid, nRows, nCols):
  #Find a random starting cell that is empty.
  while True:
    row = random.randrange(nRows)
    col = random.randrange(nCols)
    if(aGrid[row][col] == EMPTY):
      return row, col

for item in whatToAddInGrid:
  rowRandom, colRandom = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
  grid[rowRandom][colRandom] = item


for row in grid:
  print(row)

#Setting the starting cell
startRow, startCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
print('Starting at row:', startRow, 'col:', startCol)

score = 0
sword = []
potion = []
while True:
  #move the user around
  direction = input('Press L, U, R, D to move: ').lower()
  print()

  if(direction == 'l'):
    if(startCol == 0):
      startCol = NCOLS_IN_GRID - 1
    else:
      startCol -= 1 
  elif (direction == 'r'):
    if(startCol == NCOLS_IN_GRID - 1):
      startCol = 0
    else:
      startCol += 1      
  elif(direction == 'u'):
    if(startRow == 0):
      startRow = NROWS_IN_GRID - 1
    else:
      startRow -= 1 
  elif(direction == 'd'):
    if(startRow == NROWS_IN_GRID - 1):
      startRow = 0
    else:
      startRow += 1  
  else:
    print('Invalid move. Quitting the game.')
    break

  foundInCell = grid[startRow][startCol]
  print('Now at row', startRow, ' col:', startCol, ' cell contains:', foundInCell)
  if "t" in foundInCell:
    score +=1
    grid[startRow][startCol] = EMPTY 
    print("The current Score is: ",score)
  
  if "s" in foundInCell:
    sword.append(SWORD)
    print("You have sword item")
  
  if "m" in foundInCell:
    if len(sword) == False:
      print("Monster killed you. ")
      break
    else:
      sword.clear()
      grid[startRow][startCol] = EMPTY 
    print("You used sword")

  if "p" in foundInCell:
    potion.append(POTION)
    print("You have potion and you can protect yourself against venom")
  
  if "v" in foundInCell:
    if len(potion) == False:
      print("Venom killed you. ")
      break
    else:
      potion.clear()
      grid[startRow][startCol] = EMPTY 
    print("You used potion")
    
