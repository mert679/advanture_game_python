import fileIoHelper as fh
import random
import json
from datetime import datetime
timeNow1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


#FILE_PATH = "result.json"

EMPTY = 'e'
TREASURE = 't'
MONSTER = 'm'
VENOM = "v"
SWORD = 's'
POTION ='p'
# 2treasure ekledim 2 monster 1 potion 
whatToAddInGrid = (TREASURE, TREASURE, TREASURE,TREASURE,TREASURE, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER,SWORD, SWORD, POTION, POTION,POTION,VENOM,VENOM,VENOM)


NROWS_IN_GRID = 6
NCOLS_IN_GRID = 7

grid = []
clone_grid =[]
for r in range(0, NROWS_IN_GRID): #0-5
  aRow = []
  #added
  bRow = []
  for c in range(0, NCOLS_IN_GRID):#0-7
    aRow.append(EMPTY)  
    bRow.append(" ")

  grid.append(aRow)
  clone_grid.append(bRow)


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


# for row in grid:
#   print(row)

#Setting the starting cell
counterr = 0
# display her çağırıldığında bir satır basıyor
def display(row , c):
  
  
  #bracket aç
  print("[",end ="")
  for i in range(len(row)):
    if clone_grid[int(c)][i] == True:
      print("'", end ="")
      print(row[i], end ="")
      print("'", end ="")
    else:
      print("' '", end ="")
    #eğer son column değlse virgul
    if i != 6:
      print(", ",end ="")

  #bracket kapa
  print("]")


sword = []
potion = []

moves = [ ]



   
counterr=0

startRow, startCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
clone_grid[startRow][startCol] = True





for row in grid:
  display(row, counterr)
  counterr+=1
  

print('Starting at row:', startRow, 'col:', startCol)



score = 0
while True:
  #move the user around
  direction = input('Press L, U, R, D to move: ').lower()

  moves.append(direction)
  print()


  if(direction == 'l'):
    if(startCol == 0):
      startCol = NCOLS_IN_GRID - 1
      clone_grid[startRow][startCol] = True
    else:
      startCol -= 1 
      clone_grid[startRow][startCol] = True

  elif (direction == 'r'):
    if(startCol == NCOLS_IN_GRID - 1):
      startCol = 0
      clone_grid[startRow][startCol] = True
    else:
      startCol += 1      
      clone_grid[startRow][startCol] = True

  elif(direction == 'u'):
    if(startRow == 0):
      startRow = NROWS_IN_GRID - 1
      clone_grid[startRow][startCol] = True
    else:
      startRow -= 1 
      clone_grid[startRow][startCol] = True

  elif(direction == 'd'):
    if(startRow == NROWS_IN_GRID - 1):
      startRow = 0
      clone_grid[startRow][startCol] = True
    else:
      startRow += 1  
      clone_grid[startRow][startCol] = True
    
    
  else:
    print('Invalid move. Quitting the game.')
    break
  
  
  
  foundInCell = grid[startRow][startCol]
  

  #print('Now at row', startRow, ' col:', startCol, ' cell contains:', foundInCell)
  
  if "e" in foundInCell:
      score +=1

  if "t" in foundInCell:
    score +=1
    # grid[startRow][startCol] = EMPTY 
    #print("The current Score is: ",score)

  if "s" in foundInCell:
    sword.append(SWORD)
    score +=1

    print("You have sword item")


  if "m" in foundInCell:
    if len(sword) == False:
      print("Monster killed you. ")
      
      
      break
    else:
      sword.pop(-1)
      # grid[startRow][startCol] = EMPTY 
      score +=1
      print("You used sword")

  if "p" in foundInCell:
    potion.append(POTION)
    score +=1
    print("You have potion to venom")

  if "v" in foundInCell:
    if len(potion) == False:
      print("Venom killed you. ")
      
      break
    else:
      potion.pop(-1)
      #grid[startRow][startCol] = EMPTY 
      score +=1
      print("You used potion")
  
  
  print("\033[H\033[J", end="")
  counterr=0
  for row in grid:
    display(row, counterr)
    counterr+=1
    
  
  
  print(f"Score:[{score}] Sword:[{len(sword)}] Potion:[{len(potion)}]")
    
      

#game()

timeNow2 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
users = { } 
times ={ }

if fh.fileExists("gamelog.json"):
  content = fh.readFile("gamelog.json")
  users = json.loads(content) 


#users["move"] = moves
#users["score"] = score
times["moves"] = moves
times["score"] = score
users[timeNow1] = times


#users[userName] = username

result = str(users).replace("'",'"')

fh.writeFile("gamelog.json",result)