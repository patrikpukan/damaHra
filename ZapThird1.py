from tk import *

screen=tk()
screen.title("Dama")
canvas=Canvas(width=600 , height=600)
canvas.pack()

# canvas.create_rectangle(100,100,200,200,fill='black')

white = {'pawn':1,
          'queen': 2}
black = {'pawn':3,
          'queen':4}


def newGame():
  """ Generates a new stock playboard. """
  global board, whiteScore, blackScore, currentPlayer, possibleDestination, possibleKillstination, enemyDestination, doubleJumpVar
  possibleDestination=[]
  possibleKillstination=[]
  enemyDestination=[]
  doubleJumpVar=0

  canvas.delete("all")
  board=[[0 for x in range(8)] for i in range(8)]
  whiteScore=0
  blackScore=0
  currentPlayer="White"
  for i in range(8):
    if i % 2 == 0:
      board[0][i]=2
      board[6][i]=1

    if i % 2 != 0:
      board[1][i]=2
      board[7][i]=1
  
  for i in board:
    print(i)
  
  playField()


def doNothing():
  pass


def endGameMenu():
  """Draws the Post-match menu."""
  global whiteScore, blackScore,board, quitButton, newGameButton, winGameButton

  canvas.delete("all")
  canvas.pack()
  canvas.create_rectangle(100,100,500,500, fill="white")
  if whiteScore == 8:
    winGameButton=Button(canvas, text="Winner is: White",width=80, height=6, command = doNothing)
  if blackScore == 8:
    winGameButton=Button(canvas, text="Winner is: Black",width=80,height=6, command = doNothing)

  newGameButton=Button(canvas, text="New Game",width=80, height=9, command = brandNewGame)
  quitButton=Button(canvas,text = "Exit Game",width=80, height=9, command = quit)
  newGameButton.place(x=20, y=100)
  quitButton.place(x=20, y=300)
  winGameButton.place(x=20,y=500)


def brandNewGame():
  global quitButton, newGameButton, winGameButton
  quitButton.destroy()
  newGameButton.destroy()
  winGameButton.destroy()
  newGame()


def checkForEnd():
  """Checks if the game is over."""
  global whiteScore,blackScore,board

  if whiteScore == 8 or blackScore == 8:
    canvas.delete("all")
    canvas.pack()
    endGameMenu()

def playField():
  """ Creates a graphical UI based on current variables. """
  canvas.delete("all")
  y=50
  for i in range(8):
    y+=50
    x=100
    for o in range(8):
      if i % 2 == 0:
        if o % 2 ==0:
          canvas.create_rectangle(x,y,x+50,y+50, fill="black")
          x+=50
        else:
          canvas.create_rectangle(x,y,x+50,y+50, fill="red")
          x+=50
      else:
        if o % 2 ==0:
          canvas.create_rectangle(x,y,x+50,y+50, fill="red")
          x+=50
        else:
          canvas.create_rectangle(x,y,x+50,y+50, fill="black")
          x+=50
        
  for m in range(8):
    for n in range(8):
      if board[m][n] == 1:
        canvas.create_oval(100+(n*50),100+(m*50), 150+(n*50),150+(m*50), fill="white")
      if board[m][n] == 2:
        canvas.create_oval(100+(n*50),100+(m*50), 150+(n*50),150+(m*50), fill="black", outline="grey", width=3)
      if board[m][n] == 3:
        canvas.create_oval(100+(n*50),100+(m*50), 150+(n*50),150+(m*50), fill="white", outline="red", width=3)
      if board[m][n] == 4:
        canvas.create_oval(100+(n*50),100+(m*50), 150+(n*50),150+(m*50), fill="black",outline="white", width=3)

  canvas.create_text(300,540, text=f"Current Player: {currentPlayer}", font=60)
  canvas.create_text(100, 540, text=f"White's score: {whiteScore}", font=60)
  canvas.create_text(500, 540, text=f"Black's score: {blackScore}", font=60)

  cancelButton=Button(canvas, text="Cancel Choice",width=20, command = cancelChoice)
  swapButton=Button(canvas,text = "Swap Sides",width=20, command = changePlayer)
  cancelButton.place(x=100, y=50)
  swapButton.place(x=350, y=50)
  for i in board:
    print(i)
  print()


def cancelChoice():
  """Cancel player's current choice."""
  global enemyDestination,possibleDestination,possibleKillstination,possibleMoves,possibleMovesQueen, doubleJumpVar, currentPlayer

  if doubleJumpVar==1:
    changePlayer()
  possibleDestination=[]
  possibleKillstination=[]
  enemyDestination=[]
  doubleJumpVar=0
  playField()


def changePlayer():
  """ Changes the current player to the other one. """
  global currentPlayer, doubleJumpVar

  if currentPlayer=="White":
    currentPlayer="Black"
    doubleJumpVar=0
    playField()
    return

  if currentPlayer=="Black":
    currentPlayer="White"
    doubleJumpVar=0
    playField()
    return
  

def checkIfBecomeQueen():
  """Checks if any pawn has become a queen in this round."""
  global currentPlayer

  if currentPlayer=="White":
    for i in range(8):
      if board[0][i]==1:
        board[0][i]=3

  if currentPlayer=="Black":
    for o in range(8):
      if board[7][o]==2:
        board[7][o]=4
  
  playField()


def doubleJumpPossibility(x,y):
  """Checks if a piece can jump multiple times."""
  global board,possibleKillstination, enemyDestination, currentPlayer, doubleJumpVar, currentLoc

  if currentPlayer=="White":
    if board[y][x]==1:
      possibleMovesDJ(x,y)
      if possibleKillstination != []:
        doubleJumpVar = 1
        currentLoc=[x,y]
      else:
        doubleJumpVar = 0
    if board[y][x]==3:
      possibleMovesQueenDJ(x,y)
      if possibleKillstination != []:
        doubleJumpVar = 1
        currentLoc=[x,y]
      else:
        doubleJumpVar = 0

  if currentPlayer=="Black":
    if board[y][x]==2:
      possibleMovesDJ(x,y)
      if possibleKillstination != []:
        doubleJumpVar = 1
        currentLoc=[x,y]
      else:
        doubleJumpVar = 0
    if board[y][x]==4:
      possibleMovesQueenDJ(x,y)
      if possibleKillstination != []:
        doubleJumpVar = 1
        currentLoc=[x,y]
      else:
        doubleJumpVar = 0

  # print(doubleJumpVar, "xd")


def move(x,y):
  """Non-lethal move logic."""
  global possibleDestination,enemyDestination, possibleKillstination, currentLoc, currentPlayer

  if currentPlayer=="White":
    if [x,y] in possibleDestination:
      if board[currentLoc[1]][currentLoc[0]]==1:
        board[currentLoc[1]][currentLoc[0]]=0
        board[y][x]=1
      
      if board[currentLoc[1]][currentLoc[0]]==3:
        board[currentLoc[1]][currentLoc[0]]=0
        board[y][x]=3

  if currentPlayer=="Black":
    if [x,y] in possibleDestination:
      if board[currentLoc[1]][currentLoc[0]]==2:
        board[currentLoc[1]][currentLoc[0]]=0
        board[y][x]=2
      
      if board[currentLoc[1]][currentLoc[0]]==4:
        board[currentLoc[1]][currentLoc[0]]=0
        board[y][x]=4

  checkIfBecomeQueen()
  changePlayer()
  playField()
  checkForEnd()


def kickMove(x,y):
  """Lethal move logic."""
  global possibleKillstination,currentLoc, currentPlayer,enemyDestination, whiteScore, blackScore, doubleJumpVar

  if currentPlayer=="White":
    for v in range(len(possibleKillstination)):
      print(f"possibleKillstination[{v}]: {possibleKillstination[v]}")
      print(f"enemyDestination: {enemyDestination}")
      if possibleKillstination[v]==[x,y]:
        if board[currentLoc[1]][currentLoc[0]]==1:
          board[currentLoc[1]][currentLoc[0]]=0
          board[enemyDestination[v][1]][enemyDestination[v][0]]=0
          board[y][x]=1
          whiteScore+=1
          checkIfBecomeQueen()
          doubleJumpPossibility(x,y)
          if doubleJumpVar == 0:
            changePlayer()
            playField()
          checkForEnd()
          return
          
        if board[currentLoc[1]][currentLoc[0]]==3:
          board[currentLoc[1]][currentLoc[0]]=0
          board[enemyDestination[v][1]][enemyDestination[v][0]]=0
          board[y][x]=3
          whiteScore+=1
          checkIfBecomeQueen()
          doubleJumpPossibility(x,y)
          if doubleJumpVar == 0:
            changePlayer()
            playField()
          checkForEnd()
          return
          

  if currentPlayer=="Black":
    for w in range(len(possibleKillstination)):
      print(f"possibleKillstination[{w}]: {possibleKillstination[w]}")
      print(f"enemyDestination: {enemyDestination}")
      if possibleKillstination[w]==[x,y]:
        if board[currentLoc[1]][currentLoc[0]]==2:
          board[currentLoc[1]][currentLoc[0]]=0
          board[enemyDestination[w][1]][enemyDestination[w][0]]=0
          board[y][x]=2
          blackScore+=1
          checkIfBecomeQueen()
          doubleJumpPossibility(x,y)
          if doubleJumpVar == 0:
            changePlayer()
            playField()
          checkForEnd()
          return
        if board[currentLoc[1]][currentLoc[0]]==4:
          board[currentLoc[1]][currentLoc[0]]=0
          board[enemyDestination[w][1]][enemyDestination[w][0]]=0
          board[y][x]=4
          blackScore+=1
          checkIfBecomeQueen()
          doubleJumpPossibility(x,y)
          if doubleJumpVar == 0:
            changePlayer()
            playField()
          checkForEnd()
          return


def possibleMoves(x,y):
  """Shows possible moves for a clicked pawn piece by painting possible destinations green. """
  global board,possibleDestination,enemyDestination,possibleKillstination
  possibleDestination=[]
  enemyDestination=[]
  possibleKillstination=[]
  playField()

  if currentPlayer=="White":
    if board[y][x]==1:
      try:
        if board[y-1][x-1]==0:
          if x != 0:
            possibleDestination.append([x-1,y-1])
            canvas.create_rectangle(100+((x-1)*50), 100+((y-1)*50),150+((x-1)*50), 150+((y-1)*50), fill="green")
      except:
        pass
      try:
        if board[y-1][x+1]==0:
          possibleDestination.append([x+1,y-1])
          canvas.create_rectangle(100+((x+1)*50), 100+((y-1)*50),150+((x+1)*50), 150+((y-1)*50), fill="green")
      except:
        pass
      try:
        if board[y-1][x-1]==2 or board[y-1][x-1]==4:
          if x != 0 and x != 1:
            if board[y-2][x-2]==0:
              enemyDestination.append([x-1,y-1])
              possibleKillstination.append([x-2,y-2])
              canvas.create_rectangle(100+((x-2)*50), 100+((y-2)*50),150+((x-2)*50), 150+((y-2)*50), fill="blue")
      except:
        pass
      try:
        if board[y-1][x+1]==2 or board[y-1][x+1]==4:
          if board[y-2][x+2]==0:
            enemyDestination.append([x+1,y-1])
            possibleKillstination.append([x+2,y-2])
            canvas.create_rectangle(100+((x+2)*50), 100+((y-2)*50),150+((x+2)*50), 150+((y-2)*50), fill="blue")
      except:
        pass

  if currentPlayer=="Black":
    if board[y][x]==2:
      try:
        if board[y+1][x-1]==0:
          if x != 0:
            possibleDestination.append([x-1,y+1])
            canvas.create_rectangle(100+((x-1)*50), 100+((y+1)*50),150+((x-1)*50), 150+((y+1)*50), fill="green")
      except:
        pass
      try:
        if board[y+1][x+1]==0:
          possibleDestination.append([x+1,y+1])
          canvas.create_rectangle(100+((x+1)*50), 100+((y+1)*50),150+((x+1)*50), 150+((y+1)*50), fill="green")
      except:
        pass
      try:
        if board[y+1][x-1]==1 or board[y+1][x-1]==3:
          if x != 0 and x != 1:
            if board[y+2][x-2]==0:
              enemyDestination.append([x-1,y+1])
              possibleKillstination.append([x-2,y+2])
              canvas.create_rectangle(100+((x-2)*50), 100+((y+2)*50),150+((x-2)*50), 150+((y+2)*50), fill="blue")
      except:
        pass
      try:
        if board[y+1][x+1]==1 or board[y+1][x+1]==3:
          if board[y+2][x+2]==0:
            enemyDestination.append([x+1,y+1])
            possibleKillstination.append([x+2,y+2])
            canvas.create_rectangle(100+((x+2)*50), 100+((y+2)*50),150+((x+2)*50), 150+((y+2)*50), fill="blue")
      except:
        pass
     

  print(f"possibleDestination: {possibleDestination}")
  print(f"possibleKillstination: {possibleKillstination}")
  print(f"enemyDestination: {enemyDestination}")


def possibleMovesQueen(x,y):
  """Shows possible moves for a clicked queen piece by painting possible destinations green. """
  global possibleDestination, enemyDestination, possibleKillstination
  possibleDestination=[]
  enemyDestination=[]
  possibleKillstination=[]
  i=1
  i2=1
  i3=1
  i4=1
  playField()

  if currentPlayer=="White":
    if board[y][x]==3:
      try:
        if board[y+i][x+i]==2 or board[y+i][x+i]==4:
          if board[y+i+1][x+i+1] == 0:
            if (x+i+1) <=7 and (y+i+1) <=7:
              enemyDestination.append([x+i,y+i])
              possibleKillstination.append([x+i+1,y+i+1])
              canvas.create_rectangle(100+((x+i+1)*50), 100+((y+i+1)*50),150+((x+i+1)*50), 150+((y+i+1)*50), fill="blue")
        while board[y+i][x+i]==0:
          # South East Check
          if x == 7 or y == 7:
            break
          if board[y+i][x+i]==0:
            possibleDestination.append([x+i,y+i])
            canvas.create_rectangle(100+((x+i)*50), 100+((y+i)*50),150+((x+i)*50), 150+((y+i)*50), fill="green")
            if (x+i)==7 or (y+i)==7:
              break
          if board[y+i+1][x+i+1] != 0:
            if board[y+i+1][x+i+1]==2 or board[y+i+1][x+i+1]==4:
              if (x+i+2)>7 or (y+i+2)>7:
                break
              if board[y+i+2][x+i+2]==0:
                enemyDestination.append([x+i+1,y+i+1])
                possibleKillstination.append([x+i+2,y+i+2])
                canvas.create_rectangle(100+((x+i+2)*50), 100+((y+i+2)*50),150+((x+i+2)*50), 150+((y+i+2)*50), fill="blue")
                break
            else:
              break
          i+=1

      except:
        pass

      try:
        if board[y+i2][x-i2]==2 or board[y+i2][x-i2]==4:
          if board[y+i2+1][x-i2-1]==0:
            if (x-i2-1) >= 0 and (y+i2+1) <=7:
              enemyDestination.append([x-i2,y+i2])
              possibleKillstination.append([x-i2-1,y+i2+1])
              canvas.create_rectangle(100+((x-i2-1)*50), 100+((y+i2+1)*50),150+((x-i2-1)*50), 150+((y+i2+1)*50), fill="blue")
        while board[y+i2][x-i2]==0:
          # South West Check
          if x == 0 or y == 7:
            break
          if board[y+i2][x-i2]==0:
            possibleDestination.append([x-i2,y+i2])
            canvas.create_rectangle(100+((x-i2)*50), 100+((y+i2)*50),150+((x-i2)*50), 150+((y+i2)*50), fill="green")
            if (x-i2)==0 or (y+i2)==7:
              break
          if board[y+i2+1][x-i2-1] != 0:
            if board[y+i2+1][x-i2-1]==2 or board[y+i2+1][x-i2-1]==4:
              if (x-i2-2) < 0 or (y+i2+2) >7:
                break
              if board[y+i2+2][x-i2-2]==0:
                enemyDestination.append([x-i2-1,y+i2+1])
                possibleKillstination.append([x-i2-2,y+i2+2])
                canvas.create_rectangle(100+((x-i2-2)*50), 100+((y+i2+2)*50),150+((x-i2-2)*50), 150+((y+i2+2)*50), fill="blue")
                break
            else:
              break
          i2+=1
      except:
        pass

      try:
        if board[y-i3][x-i3]==2 or board[y-i3][x-i3]==4:
          if board[y-i3-1][x-i3-1]==0:
            if (x-i3-1) >= 0 and (y-i3-1) >= 0:
              enemyDestination.append([x-i3,y-i3])
              possibleKillstination.append([x-i3-1,y-i3-1])
              canvas.create_rectangle(100+((x-i3-1)*50), 100+((y-i3-1)*50),150+((x-i3-1)*50), 150+((y-i3-1)*50), fill="blue")
        while board[y-i3][x-i3]==0:
          # North West Check
          if x == 0 or y == 0:
            break
          if board[y-i3][x-i3]==0:
            possibleDestination.append([x-i3,y-i3])
            canvas.create_rectangle(100+((x-i3)*50), 100+((y-i3)*50),150+((x-i3)*50), 150+((y-i3)*50), fill="green")
            if (x-i3)==0 or (y-i3)==0:
              break
          if board[y-i3-1][x-i3-1] != 0:
            if board[y-i3-1][x-i3-1]==2 or board[y-i3-1][x-i3-1]==4:
              if (x-i3-2) < 0 or (y-i3-2) < 0:
                break
              if board[y-i3-2][x-i3-2]==0:
                enemyDestination.append([x-i3-1,y-i3-1])
                possibleKillstination.append([x-i3-2,y-i3-2])
                canvas.create_rectangle(100+((x-i3-2)*50), 100+((y-i3-2)*50),150+((x-i3-2)*50), 150+((y-i3-2)*50), fill="blue")
                break
            else:
              break
          i3+=1
      except:
        pass

      try:
        if board[y-i4][x+i4]==2 or board[y-i4][x+i4]==4:
          if board[y-i4-1][x+i4+1]==0:
            if (x+i4+1) <=7 and (y-i4-1) >= 0:
              enemyDestination.append([x+i4,y-i4])
              possibleKillstination.append([x+i4+1,y-i4-1])
              canvas.create_rectangle(100+((x+i4+1)*50), 100+((y-i4-1)*50),150+((x+i4+1)*50), 150+((y-i4-1)*50), fill="blue")
        while board[y-i4][x+i4]==0:
          # North East Check
          if x == 7 or y  == 0:
            break
          if board[y-i4][x+i4]==0:
            possibleDestination.append([x+i4,y-i4])
            canvas.create_rectangle(100+((x+i4)*50), 100+((y-i4)*50),150+((x+i4)*50), 150+((y-i4)*50), fill="green")
            if (x+i4)==7 or (y-i4)==0:
              break
          if board[y-i4-1][x+i4+1] != 0:
            if board[y-i4-1][x+i4+1]==2 or board[y-i4-1][x+i4+1]==4:
              if (x+i4+2)>7 or (y-i4-2) < 0:
                break
              if board[y-i4-2][x+i4+2]==0:
                enemyDestination.append([x+i4+1,y-i4-1])
                possibleKillstination.append([x+i4+2,y-i4-2])
                canvas.create_rectangle(100+((x+i4+2)*50), 100+((y-i4-2)*50),150+((x+i4+2)*50), 150+((y-i4-2)*50), fill="blue")
                break
            else:
              break
          i4+=1
      except:
        pass
  
  if currentPlayer=="Black":
    if board[y][x]==4:
      try:
        if board[y+i][x+i]==1 or board[y+i][x+i]==3:
          if board[y+i+1][x+i+1] == 0:
            if (x+i+1) <=7 and (y+i+1) <=7:
              enemyDestination.append([x+i,y+i])
              possibleKillstination.append([x+i+1,y+i+1])
              canvas.create_rectangle(100+((x+i+1)*50), 100+((y+i+1)*50),150+((x+i+1)*50), 150+((y+i+1)*50), fill="blue")
        while board[y+i][x+i]==0:
          # South East Check
          if x == 7 or y == 7:
            break
          if board[y+i][x+i]==0:
            possibleDestination.append([x+i,y+i])
            canvas.create_rectangle(100+((x+i)*50), 100+((y+i)*50),150+((x+i)*50), 150+((y+i)*50), fill="green")
            if (x+i)==7 or (y+i)==7:
              break
          if board[y+i+1][x+i+1] != 0:
            if board[y+i+1][x+i+1]==1 or board[y+i+1][x+i+1]==3:
              if (x+i+2)>7 or (y+i+2)>7:
                break
              if board[y+i+2][x+i+2]==0:
                enemyDestination.append([x+i+1,y+i+1])
                possibleKillstination.append([x+i+2,y+i+2])
                canvas.create_rectangle(100+((x+i+2)*50), 100+((y+i+2)*50),150+((x+i+2)*50), 150+((y+i+2)*50), fill="blue")
                break
            else:
              break
          i+=1

      except:
        pass

      try:
        if board[y+i2][x-i2]==1 or board[y+i2][x-i2]==3:
          if board[y+i2+1][x-i2-1]==0:
            if (x-i2-1) >= 0 and (y+i2+1) <=7:
              enemyDestination.append([x-i2,y+i2])
              possibleKillstination.append([x-i2-1,y+i2+1])
              canvas.create_rectangle(100+((x-i2-1)*50), 100+((y+i2+1)*50),150+((x-i2-1)*50), 150+((y+i2+1)*50), fill="blue")
        while board[y+i2][x-i2]==0:
          # South West Check
          if x == 0 or y == 7:
            break
          if board[y+i2][x-i2]==0:
            possibleDestination.append([x-i2,y+i2])
            canvas.create_rectangle(100+((x-i2)*50), 100+((y+i2)*50),150+((x-i2)*50), 150+((y+i2)*50), fill="green")
            if (x-i2)==0 or (y+i2)==7:
              break
          if board[y+i2+1][x-i2-1] != 0:
            if board[y+i2+1][x-i2-1]==1 or board[y+i2+1][x-i2-1]==3:
              if (x-i2-2) < 0 or (y+i2+2) >7:
                break
              if board[y+i2+2][x-i2-2]==0:
                enemyDestination.append([x-i2-1,y+i2+1])
                possibleKillstination.append([x-i2-2,y+i2+2])
                canvas.create_rectangle(100+((x-i2-2)*50), 100+((y+i2+2)*50),150+((x-i2-2)*50), 150+((y+i2+2)*50), fill="blue")
                break
            else:
              break
          i2+=1
      except:
        pass

      try:
        if board[y-i3][x-i3]==1 or board[y-i3][x-i3]==3:
          if board[y-i3-1][x-i3-1]==0:
            if (x-i3-1) >= 0 and (y-i3-1) >= 0:
              enemyDestination.append([x-i3,y-i3])
              possibleKillstination.append([x-i3-1,y-i3-1])
              canvas.create_rectangle(100+((x-i3-1)*50), 100+((y-i3-1)*50),150+((x-i3-1)*50), 150+((y-i3-1)*50), fill="blue")
        while board[y-i3][x-i3]==0:
          # North West Check
          if x == 0 or y == 0:
            break
          if board[y-i3][x-i3]==0:
            possibleDestination.append([x-i3,y-i3])
            canvas.create_rectangle(100+((x-i3)*50), 100+((y-i3)*50),150+((x-i3)*50), 150+((y-i3)*50), fill="green")
            if (x-i3)==0 or (y-i3)==0:
              break
          if board[y-i3-1][x-i3-1] != 0:
            if board[y-i3-1][x-i3-1]==1 or board[y-i3-1][x-i3-1]==3:
              if (x-i3-2) < 0 or (y-i3-2) < 0:
                break
              if board[y-i3-2][x-i3-2]==0:
                enemyDestination.append([x-i3-1,y-i3-1])
                possibleKillstination.append([x-i3-2,y-i3-2])
                canvas.create_rectangle(100+((x-i3-2)*50), 100+((y-i3-2)*50),150+((x-i3-2)*50), 150+((y-i3-2)*50), fill="blue")
                break
            else:
              break
          i3+=1
      except:
        pass

      try:
        if board[y-i4][x+i4]==1 or board[y-i4][x+i4]==3:
          if board[y-i4-1][x+i4+1]==0:
            if (x+i4+1) <=7 and (y-i4-1) >= 0:
              enemyDestination.append([x+i4,y-i4])
              possibleKillstination.append([x+i4+1,y-i4-1])
              canvas.create_rectangle(100+((x+i4+1)*50), 100+((y-i4-1)*50),150+((x+i4+1)*50), 150+((y-i4-1)*50), fill="blue")
        while board[y-i4][x+i4]==0:
          # North East Check
          if x == 7 or y  == 0:
            break
          if board[y-i4][x+i4]==0:
            possibleDestination.append([x+i4,y-i4])
            canvas.create_rectangle(100+((x+i4)*50), 100+((y-i4)*50),150+((x+i4)*50), 150+((y-i4)*50), fill="green")
            if (x+i4)==7 or (y-i4)==0:
              break
          if board[y-i4-1][x+i4+1] != 0:
            if board[y-i4-1][x+i4+1]==1 or board[y-i4-1][x+i4+1]==3:
              if (x+i4+2)>7 or (y-i4-2) < 0:
                break
              if board[y-i4-2][x+i4+2]==0:
                enemyDestination.append([x+i4+1,y-i4-1])
                possibleKillstination.append([x+i4+2,y-i4-2])
                canvas.create_rectangle(100+((x+i4+2)*50), 100+((y-i4-2)*50),150+((x+i4+2)*50), 150+((y-i4-2)*50), fill="blue")
                break
            else:
              break
          i4+=1
      except:
        pass
  
      
  
      
  

  print(f"possibleDestination: {possibleDestination}")
  print(f"possibleKillstination: {possibleKillstination}")
  print(f"enemyDestination: {enemyDestination}")


def possibleMovesDJ(x,y):
  """Shows possible moves for a clicked pawn piece by painting possible destinations green. (DURING A DOUBLE JUMP) """
  global board,possibleDestination,enemyDestination,possibleKillstination
  possibleDestination=[]
  enemyDestination=[]
  possibleKillstination=[]
  playField()

  if currentPlayer=="White":
    if board[y][x]==1:
      try:
        if board[y-1][x-1]==2 or board[y-1][x-1]==4:
          if x != 0 and x != 1:
            if board[y-2][x-2]==0:
              enemyDestination.append([x-1,y-1])
              possibleKillstination.append([x-2,y-2])
              canvas.create_rectangle(100+((x-2)*50), 100+((y-2)*50),150+((x-2)*50), 150+((y-2)*50), fill="blue")
      except:
        pass
      try:
        if board[y-1][x+1]==2 or board[y-1][x+1]==4:
          if board[y-2][x+2]==0:
            enemyDestination.append([x+1,y-1])
            possibleKillstination.append([x+2,y-2])
            canvas.create_rectangle(100+((x+2)*50), 100+((y-2)*50),150+((x+2)*50), 150+((y-2)*50), fill="blue")
      except:
        pass

  if currentPlayer=="Black":
    if board[y][x]==2:
      try:
        if board[y+1][x-1]==1 or board[y+1][x-1]==3:
          if x != 0 and x != 1:
            if board[y+2][x-2]==0:
              enemyDestination.append([x-1,y+1])
              possibleKillstination.append([x-2,y+2])
              canvas.create_rectangle(100+((x-2)*50), 100+((y+2)*50),150+((x-2)*50), 150+((y+2)*50), fill="blue")
      except:
        pass
      try:
        if board[y+1][x+1]==1 or board[y+1][x+1]==3:
          if board[y+2][x+2]==0:
            enemyDestination.append([x+1,y+1])
            possibleKillstination.append([x+2,y+2])
            canvas.create_rectangle(100+((x+2)*50), 100+((y+2)*50),150+((x+2)*50), 150+((y+2)*50), fill="blue")
      except:
        pass
     

  print(f"possibleDestination: {possibleDestination}")
  print(f"possibleKillstination: {possibleKillstination}")
  print(f"enemyDestination: {enemyDestination}")


def possibleMovesQueenDJ(x,y):
  """Shows possible moves for a clicked queen piece by painting possible destinations green. (DURING A DOUBLE JUMP) """
  global possibleDestination, enemyDestination, possibleKillstination
  possibleDestination=[]
  enemyDestination=[]
  possibleKillstination=[]
  i=1
  i2=1
  i3=1
  i4=1
  playField()

  if currentPlayer=="White":
    if board[y][x]==3:
      try:
        if board[y+i][x+i]==2 or board[y+i][x+i]==4:
          if board[y+i+1][x+i+1] == 0:
            if (x+i+1) <=7 and (y+i+1) <=7:
              enemyDestination.append([x+i,y+i])
              possibleKillstination.append([x+i+1,y+i+1])
              canvas.create_rectangle(100+((x+i+1)*50), 100+((y+i+1)*50),150+((x+i+1)*50), 150+((y+i+1)*50), fill="blue")
        while board[y+i][x+i]==0:
          # South East Check
          if x == 7 or y == 7:
            break
          if board[y+i][x+i]==0:
            if (x+i)==7 or (y+i)==7:
              break
          if board[y+i+1][x+i+1] != 0:
            if board[y+i+1][x+i+1]==2 or board[y+i+1][x+i+1]==4:
              if (x+i+2)>7 or (y+i+2)>7:
                break
              if board[y+i+2][x+i+2]==0:
                enemyDestination.append([x+i+1,y+i+1])
                possibleKillstination.append([x+i+2,y+i+2])
                canvas.create_rectangle(100+((x+i+2)*50), 100+((y+i+2)*50),150+((x+i+2)*50), 150+((y+i+2)*50), fill="blue")
                break
            else:
              break
          i+=1

      except:
        pass

      try:
        if board[y+i2][x-i2]==2 or board[y+i2][x-i2]==4:
          if board[y+i2+1][x-i2-1]==0:
            if (x-i2-1) >= 0 and (y+i2+1) <=7:
              enemyDestination.append([x-i2,y+i2])
              possibleKillstination.append([x-i2-1,y+i2+1])
              canvas.create_rectangle(100+((x-i2-1)*50), 100+((y+i2+1)*50),150+((x-i2-1)*50), 150+((y+i2+1)*50), fill="blue")
        while board[y+i2][x-i2]==0:
          # South West Check
          if x == 0 or y == 7:
            break
          if board[y+i2][x-i2]==0:
            if (x-i2)==0 or (y+i2)==7:
              break
          if board[y+i2+1][x-i2-1] != 0:
            if board[y+i2+1][x-i2-1]==2 or board[y+i2+1][x-i2-1]==4:
              if (x-i2-2) < 0 or (y+i2+2) >7:
                break
              if board[y+i2+2][x-i2-2]==0:
                enemyDestination.append([x-i2-1,y+i2+1])
                possibleKillstination.append([x-i2-2,y+i2+2])
                canvas.create_rectangle(100+((x-i2-2)*50), 100+((y+i2+2)*50),150+((x-i2-2)*50), 150+((y+i2+2)*50), fill="blue")
                break
            else:
              break
          i2+=1
      except:
        pass

      try:
        if board[y-i3][x-i3]==2 or board[y-i3][x-i3]==4:
          if board[y-i3-1][x-i3-1]==0:
            if (x-i3-1) >= 0 and (y-i3-1) >= 0:
              enemyDestination.append([x-i3,y-i3])
              possibleKillstination.append([x-i3-1,y-i3-1])
              canvas.create_rectangle(100+((x-i3-1)*50), 100+((y-i3-1)*50),150+((x-i3-1)*50), 150+((y-i3-1)*50), fill="blue")
        while board[y-i3][x-i3]==0:
          # North West Check
          if x == 0 or y == 0:
            break
          if board[y-i3][x-i3]==0:
            if (x-i3)==0 or (y-i3)==0:
              break
          if board[y-i3-1][x-i3-1] != 0:
            if board[y-i3-1][x-i3-1]==2 or board[y-i3-1][x-i3-1]==4:
              if (x-i3-2) < 0 or (y-i3-2) < 0:
                break
              if board[y-i3-2][x-i3-2]==0:
                enemyDestination.append([x-i3-1,y-i3-1])
                possibleKillstination.append([x-i3-2,y-i3-2])
                canvas.create_rectangle(100+((x-i3-2)*50), 100+((y-i3-2)*50),150+((x-i3-2)*50), 150+((y-i3-2)*50), fill="blue")
                break
            else:
              break
          i3+=1
      except:
        pass

      try:
        if board[y-i4][x+i4]==2 or board[y-i4][x+i4]==4:
          if board[y-i4-1][x+i4+1]==0:
            if (x+i4+1) <=7 and (y-i4-1) >= 0:
              enemyDestination.append([x+i4,y-i4])
              possibleKillstination.append([x+i4+1,y-i4-1])
              canvas.create_rectangle(100+((x+i4+1)*50), 100+((y-i4-1)*50),150+((x+i4+1)*50), 150+((y-i4-1)*50), fill="blue")
        while board[y-i4][x+i4]==0:
          # North East Check
          if x == 7 or y  == 0:
            break
          if board[y-i4][x+i4]==0:
            if (x+i4)==7 or (y-i4)==0:
              break
          if board[y-i4-1][x+i4+1] != 0:
            if board[y-i4-1][x+i4+1]==2 or board[y-i4-1][x+i4+1]==4:
              if (x+i4+2)>7 or (y-i4-2) < 0:
                break
              if board[y-i4-2][x+i4+2]==0:
                enemyDestination.append([x+i4+1,y-i4-1])
                possibleKillstination.append([x+i4+2,y-i4-2])
                canvas.create_rectangle(100+((x+i4+2)*50), 100+((y-i4-2)*50),150+((x+i4+2)*50), 150+((y-i4-2)*50), fill="blue")
                break
            else:
              break
          i4+=1
      except:
        pass
  
  if currentPlayer=="Black":
    if board[y][x]==4:
      try:
        if board[y+i][x+i]==1 or board[y+i][x+i]==3:
          if board[y+i+1][x+i+1] == 0:
            if (x+i+1) <=7 and (y+i+1) <=7:
              enemyDestination.append([x+i,y+i])
              possibleKillstination.append([x+i+1,y+i+1])
              canvas.create_rectangle(100+((x+i+1)*50), 100+((y+i+1)*50),150+((x+i+1)*50), 150+((y+i+1)*50), fill="blue")
        while board[y+i][x+i]==0:
          # South East Check
          if x == 7 or y == 7:
            break
          if board[y+i][x+i]==0:
            if (x+i)==7 or (y+i)==7:
              break
          if board[y+i+1][x+i+1] != 0:
            if board[y+i+1][x+i+1]==1 or board[y+i+1][x+i+1]==3:
              if (x+i+2)>7 or (y+i+2)>7:
                break
              if board[y+i+2][x+i+2]==0:
                enemyDestination.append([x+i+1,y+i+1])
                possibleKillstination.append([x+i+2,y+i+2])
                canvas.create_rectangle(100+((x+i+2)*50), 100+((y+i+2)*50),150+((x+i+2)*50), 150+((y+i+2)*50), fill="blue")
                break
            else:
              break
          i+=1

      except:
        pass

      try:
        if board[y+i2][x-i2]==1 or board[y+i2][x-i2]==3:
          if board[y+i2+1][x-i2-1]==0:
            if (x-i2-1) >= 0 and (y+i2+1) <=7:
              enemyDestination.append([x-i2,y+i2])
              possibleKillstination.append([x-i2-1,y+i2+1])
              canvas.create_rectangle(100+((x-i2-1)*50), 100+((y+i2+1)*50),150+((x-i2-1)*50), 150+((y+i2+1)*50), fill="blue")
        while board[y+i2][x-i2]==0:
          # South West Check
          if x == 0 or y == 7:
            break
          if board[y+i2][x-i2]==0:
            if (x-i2)==0 or (y+i2)==7:
              break
          if board[y+i2+1][x-i2-1] != 0:
            if board[y+i2+1][x-i2-1]==1 or board[y+i2+1][x-i2-1]==3:
              if (x-i2-2) < 0 or (y+i2+2) >7:
                break
              if board[y+i2+2][x-i2-2]==0:
                enemyDestination.append([x-i2-1,y+i2+1])
                possibleKillstination.append([x-i2-2,y+i2+2])
                canvas.create_rectangle(100+((x-i2-2)*50), 100+((y+i2+2)*50),150+((x-i2-2)*50), 150+((y+i2+2)*50), fill="blue")
                break
            else:
              break
          i2+=1
      except:
        pass

      try:
        if board[y-i3][x-i3]==1 or board[y-i3][x-i3]==3:
          if board[y-i3-1][x-i3-1]==0:
            if (x-i3-1) >= 0 and (y-i3-1) >= 0:
              enemyDestination.append([x-i3,y-i3])
              possibleKillstination.append([x-i3-1,y-i3-1])
              canvas.create_rectangle(100+((x-i3-1)*50), 100+((y-i3-1)*50),150+((x-i3-1)*50), 150+((y-i3-1)*50), fill="blue")
        while board[y-i3][x-i3]==0:
          # North West Check
          if x == 0 or y == 0:
            break
          if board[y-i3][x-i3]==0:
            if (x-i3)==0 or (y-i3)==0:
              break
          if board[y-i3-1][x-i3-1] != 0:
            if board[y-i3-1][x-i3-1]==1 or board[y-i3-1][x-i3-1]==3:
              if (x-i3-2) < 0 or (y-i3-2) < 0:
                break
              if board[y-i3-2][x-i3-2]==0:
                enemyDestination.append([x-i3-1,y-i3-1])
                possibleKillstination.append([x-i3-2,y-i3-2])
                canvas.create_rectangle(100+((x-i3-2)*50), 100+((y-i3-2)*50),150+((x-i3-2)*50), 150+((y-i3-2)*50), fill="blue")
                break
            else:
              break
          i3+=1
      except:
        pass

      try:
        if board[y-i4][x+i4]==1 or board[y-i4][x+i4]==3:
          if board[y-i4-1][x+i4+1]==0:
            if (x+i4+1) <=7 and (y-i4-1) >= 0:
              enemyDestination.append([x+i4,y-i4])
              possibleKillstination.append([x+i4+1,y-i4-1])
              canvas.create_rectangle(100+((x+i4+1)*50), 100+((y-i4-1)*50),150+((x+i4+1)*50), 150+((y-i4-1)*50), fill="blue")
        while board[y-i4][x+i4]==0:
          # North East Check
          if x == 7 or y  == 0:
            break
          if board[y-i4][x+i4]==0:
            if (x+i4)==7 or (y-i4)==0:
              break
          if board[y-i4-1][x+i4+1] != 0:
            if board[y-i4-1][x+i4+1]==1 or board[y-i4-1][x+i4+1]==3:
              if (x+i4+2)>7 or (y-i4-2) < 0:
                break
              if board[y-i4-2][x+i4+2]==0:
                enemyDestination.append([x+i4+1,y-i4-1])
                possibleKillstination.append([x+i4+2,y-i4-2])
                canvas.create_rectangle(100+((x+i4+2)*50), 100+((y-i4-2)*50),150+((x+i4+2)*50), 150+((y-i4-2)*50), fill="blue")
                break
            else:
              break
          i4+=1
      except:
        pass
  
       

  print(f"possibleDestination: {possibleDestination}")
  print(f"possibleKillstination: {possibleKillstination}")
  print(f"enemyDestination: {enemyDestination}")


def click(event):
  """Logic behind everything."""
  global board, possibleDestination, currentLoc, direction, doubleJumpVar
  
  print(f" doubleJumpVar: {doubleJumpVar}")
  if event.x > 100 and event.x < 500:
    if event.y > 100 and event.y < 500:
      xMouseCoords=(event.x - 100 ) // 50
      yMouseCoords=(event.y - 100 ) // 50
      print(f"x: {xMouseCoords}, y: {yMouseCoords}")
      print(board[yMouseCoords][xMouseCoords])

      if doubleJumpVar==0:
        for i in range(len(possibleDestination)):
          if possibleDestination[i]==[xMouseCoords,yMouseCoords]:
            move(xMouseCoords, yMouseCoords)

      for o in range(len(possibleKillstination)):
        if possibleKillstination[o]==[xMouseCoords,yMouseCoords]:
          # print("ide to")
          kickMove(xMouseCoords,yMouseCoords)

      if doubleJumpVar==0:
        if xMouseCoords >= 0 and xMouseCoords <= 7:
          if yMouseCoords >= 0 and yMouseCoords <= 7:
            if [xMouseCoords,yMouseCoords] not in possibleDestination or [xMouseCoords,yMouseCoords] not in possibleKillstination:
              if board[yMouseCoords][xMouseCoords] == 1 or board[yMouseCoords][xMouseCoords] ==2:
                currentLoc=[xMouseCoords,yMouseCoords]
                possibleMoves(xMouseCoords, yMouseCoords)
              if board[yMouseCoords][xMouseCoords] == 3 or board[yMouseCoords][xMouseCoords] ==4:
                currentLoc=[xMouseCoords,yMouseCoords]
                
                possibleMovesQueen(xMouseCoords, yMouseCoords)

      # if doubleJumpVar==1:
      #   if xMouseCoords >= 0 and xMouseCoords <= 7:
      #     if yMouseCoords >= 0 and yMouseCoords <= 7:


  




newGame()

canvas.bind("<Button-1>",click)
screen.mainloop()