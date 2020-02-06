import pygame

# Types of pieces
empty = 0
friendly = {'pawn': 1, 'queen': 3}
enemy = {'pawn': 2, 'queen': 4}

# Board size
rows = 8
columns = 8


# Create board 
def createBoard():
  board = [[empty for column in range(columns)] for row in range(rows)]
  return board


def placeStartingPieces():
  """Assign starting checker pieces for white and black"""
  # Assign starting board locations for white
  for current_row in range(7, 8):
    for current_column in range(0, 8, 2):
      board[current_row][current_column] = friendly['pawn']
  for current_row in range(6, 7):
    for current_column in range(1, 8, 2):
      board[current_row][current_column] = friendly['pawn']

  # Assign starting board locations for black
  for current_row in range(0, 1):
    for current_column in range(1, 8, 2):
      board[current_row][current_column] = enemy['pawn']
  for current_row in range(1, 2):
    for current_column in range(0, 8, 2):
      board[current_row][current_column] = enemy['pawn']


def isValidSelection(board, current_player, old_x, old_y):
  """Restricts player from slecting posisitions containing no checker pieces or """
  board_selection = board[old_y][old_x]
  if board_selection == friendly['pawn'] or friendly['queen']:
    return True
  elif board_selection == enemy['pawn'] or enemy['queen']:
    print("You've selected an enemy player's piece. Please select your own piece.")
    return False
  else:
    print("You didn't select a piece. Please try selecting one of your pieces.")
    return False


def isValidMove(current_player, board, old_x, old_y, new_x, new_y):
  """All logic for pawn pieces."""

  # Prevents moving to a location that already contains a piece.
  if board[new_y][new_x] != empty:
    print("You cant land on another piece. Please select another location.")
    return False

  # Checking for valid moves for Player 1
  if board[old_y][old_x] == 1:
    if (new_y - old_y) == -1 and (new_x - old_x) == 1:
      return True
    elif (new_y - old_y) == -1 and (new_x - old_x) == -1:
      return True
      # Checking for valid jump
    elif (new_y - old_y) == -2 and (new_x - old_x) == 2:
      if board[new_y + 1][new_x - 1] == enemy['pawn'] or enemy['queen']:
        board[new_y + 1][new_x - 1] = empty
        return True
      else:
        return False
    elif (new_y - old_y) == -2 and (new_x - old_x) == -2:
      if board[new_y + 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
        board[new_y + 1][new_x + 1] = empty
        return True
      else:
        return False
              
  # Checking for valid moves for Player 2
  elif board[old_y][old_x] == 2:
    if (new_y - old_y) == 1 and (new_x - old_x) == 1:
      return True
    elif (new_y - old_y) == 1 and (new_x - old_x) == -1:
      return True
    # Checking for valid jumps for Player 2
    elif (new_y - old_y) == 2 and (new_x - old_x) == 2:
      if board[new_y - 1][new_x - 1] == enemy['pawn'] or enemy['queen']:
        board[new_y - 1][new_x - 1] = empty
        return True
      else:
        return False
    elif (new_y - old_y) == 2 and (new_x - old_x) == -2:
      if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
        board[new_y - 1][new_x + 1] = empty
        return True
      else:
        return False
    else:
      print("You can't move that far. Please select another positition to move too.")
      return False


def noPiecesBetween(board, old_x, old_y, new_x, new_y):
  """Restricts queen pieces from jumping over several players at once"""
  board_y_coords = []
  board_x_coords = []
  if old_y < new_y:
    for row in range(old_y, new_y):
      board_y_coords.append(row)
  if old_y > new_y:
    for row in range(old_y, new_y, -1):
      board_y_coords.append(row)
  if old_x < new_x:
    for column in range(old_x, new_x):
      board_x_coords.append(column)
  if old_x > new_x:
    for column in range(old_x, new_x, -1):
      board_x_coords.append(column)

  board_coords = list(zip(board_x_coords, board_y_coords))
  board_values = [board[y][x] for x, y in board_coords]
  if len(board_values) > 2:
    if all(i == empty for i in board_values[1:-1]) is True:
      board[new_y][new_x] = board[old_y][old_x]
      board[old_y][old_x] = empty
      return True
          
  # Allows queen players to jump next to enemy pieces right next to them
  if len(board_values) == 2:
    if all(i == enemy['pawn'] for i in board_values[1:]) is True:
      board[new_y][new_x] = board[old_y][old_x]
      board[old_y][old_x] = empty
      return True
    elif all(i == enemy['queen'] for i in board_values[1:]) is True:
      board[new_y][new_x] = board[old_y][old_x]
      board[old_y][old_x] = empty
      return True
    elif all(i == empty for i in board_values[1:]) is True:
      board[new_y][new_x] = board[old_y][old_x]
      board[old_y][old_x] = empty
      return True

  # Allows queen players to move one spot over (like a pawn would move)
  elif len(board_values) == 1:
    if all(i == empty for i in board_values[1:]) is True:
      board[new_y][new_x] = board[old_y][old_x]
      board[old_y][old_x] = empty
      return True
  else:
    print("You can't jump over several chips at once. Please try another move.")
    return False


def isValidQueenMove(current_player, board, old_x, old_y, new_x, new_y):
  """All logic for queen pieces"""
  # Prevents player from jumping onto another player
  if board[new_y][new_x] != 0:
    print("Even as queen you cannot land directly onto another player's piece.")
    return False
  # Prevent horizontal moves
  if new_y == old_y:
    print("Even as a queen you cannot move horizontally in this diagonal world.")
    return False
  # Prevent horizontal moves
  if new_x == old_x:
    print("Even as a queen you cannot move vertically in this diagonal world.")
    return False
  # Prevent moves that do not have a slope of 1
  if new_x > old_x and new_y > old_y:
    if (new_x - old_x) != (new_y - old_y):
      return False
  if new_x < old_x and new_y < old_y:
    if (old_x - new_x) != (old_y - new_y):
      return False
  if new_x < old_x and new_y > old_y:
    if (old_x - new_x) != (new_y - old_y):
      return False
  if new_x > old_x and new_y < old_y:
    if (new_x - old_x) != (old_y - new_y):
      return False


  # Queen Jump Logic
  if board[old_y][old_x] == friendly['queen']:
    try: # North East Jump
      if board[new_y + 1][new_x - 1] == enemy['pawn'] or enemy['queen']:
        if old_x < new_x and old_y > new_y:
          if noPiecesBetween(board, old_x, old_y, new_x, new_y) is True:
            board[new_y][new_x] = friendly['queen']
            board[new_y + 1][new_x - 1] = empty
            board_selection = empty
            return True
    except IndexError:
      pass
    try: # North West Jump 
      if board[new_y + 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
        if old_x > new_x and old_y > new_y:
          if noPiecesBetween(board, old_x, old_y, new_x, new_y) is True:
            board[new_y][new_x] = friendly['queen']
            board[new_y + 1][new_x + 1] = empty
            board_selection = empty
            return True
    except IndexError:
      pass
    try: # South East Jump
      if board[new_y - 1][new_x - 1] == enemy['pawn'] or enemy['queen']:
        if noPiecesBetween(board, old_x, old_y, new_x, new_y) is True:
          if old_x < new_x and old_y < new_y:
            board[new_y][new_x] = friendly['queen']
            board[new_y - 1][new_x - 1] = empty
            board_selection = empty
            return True
    except IndexError:
      pass
    try: # South West Jump
      if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['pawn']:
        if noPiecesBetween(board, old_x, old_y, new_x, new_y) is True:
          if old_x > new_x and old_y < new_y:
            board[new_y][new_x] = friendly['queen']
            board[new_y - 1][new_x + 1] = empty
            board_selection = empty
            return True
    except IndexError:
      pass


def checkIfDoubleJumpPossible(board, new_x, new_y):
  # Checking for valid jump for pawns
  if current_player == 1:
    try:
      # North East
      if board[new_y - 2][new_x + 2] == empty:
        if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
          return True
      # North West
      elif board[new_y - 2][new_x - 2] == empty:
        if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
          return True
    except IndexError:
      pass
  if current_player == 2:
      try:
          # North East
          if board[new_y + 2][new_x + 2] == empty:
            if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
              return True
          # North West
          elif board[new_y + 2][new_x - 2] == empty:
            if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['queen']:
              return True
      except IndexError:
        pass
  # Checking for queen double jump possibility
  if board[new_y][new_x] == friendly['queen']:
    try:
      for i in range(8):
        # North East
        if board[new_y - i][new_x + i] == enemy['queen']:
          if board[new_y - (i+1)][new_x + (i+1)] == empty:
            return True
        # North West
        elif board[new_y - i][new_x - i] == enemy['queen']:
          if board[new_y - (i+1)][new_x - (i+1)] == empty:
            return True
        # South East
        elif board[new_y + i][new_x + i] ==  enemy['queen']:
          if board[new_y + (i+1)][new_x + (i+1)] == empty:
            return True
        # South West
        elif board[new_y + i][new_x - i] == enemy['queen']:
          if board[new_y + (i+1)][new_x - (i+1)] == empty:
            return True
    except IndexError:
      pass
  else:
    return False


def checkForWin(current_player, board):
  remaining_enemy_pieces = []
  for row in board:
    remaining_enemy_pieces.append(row.count(enemy['pawn']))
    remaining_enemy_pieces.append(row.count(enemy['queen']))
  if sum(remaining_enemy_pieces) == 0:
    print(f"Player {current_player} has won!")
    return True


def drawBoard(board):
  for row in range(8):
    for column in range(8):
      #  Variables for pygame.draw pos paramater
      # Draw all grid locations as either red or black rectangle
      if (row + column) % 2 == 0:
        color = redBg
      else:
        color = black
      rect = pygame.draw.rect(screen, color, [width * column, height * row, width, height])
      rect_center = rect.center
      if board[row][column] == 1:
        pygame.draw.circle(screen, white, rect_center, radius)
      if board[row][column] == 2:
        pygame.draw.circle(screen, black, rect_center, radius)
          # Draw border around black pieces so that they're visible
        pygame.draw.circle(screen, grey, rect_center, radius, border)
      # Drawing queen pieces borders
      if board[row][column] == 3:
        pygame.draw.circle(screen, white, rect_center, radius)
        pygame.draw.circle(screen, red, rect_center, radius, border)
      if board[row][column] == 4:
        pygame.draw.circle(screen, white, rect_center, radius, border)


# Initalize vairables
game_over = False
board = createBoard()
placeStartingPieces()

# Initalize pygame
pygame.init()

# Set the height and width of the screen
window_size = [600, 600]
screen = pygame.display.set_mode(window_size)

# Set title of screen
pygame.display.set_caption("Dama")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
dark_red = (139 , 0, 0)
grey = (128, 128, 128)
gold = (255, 215, 0)
redBg = (191, 41, 8)

# This sets the width, height and margin of each board cell
window_width = window_size[0]
window_height = window_size[1]
total_rows = 8
total_columns = 8
width = (window_width // total_columns)
height = (window_height // total_rows)

# Set the radius and border border of each checker piece
radius = (window_width // 20)
border = (window_width // 200)

# Current player turn
current_player = 1
print("White begins.") # Printing at start of the game before main loop


# Main active game loop
while not game_over:
  for event in pygame.event.get():  # User did something
    mouse_pos = pygame.mouse.get_pos()
    mouse_matrix_pos = ((mouse_pos[0] // width), (mouse_pos[1] // height)) # Matrix Cordinates of Mouse posisiton
    # print(mouse_matrix_pos)
    
    if event.type == pygame.QUIT:  # If user clicked close
      game_over = True  # Flag that the user has quit so we exit this loop


    elif event.type == pygame.MOUSEBUTTONDOWN:
      current_pos = pygame.mouse.get_pos()
      # Translating mouse x, y screen coordinates to matrix coordinates
      old_x = (current_pos[0] // width)
      old_y = (current_pos[1] // height)
      # print(f"Old coordinates: [{old_x}, {old_y}]")


      previous_piece_total = sum([sum(row) for row in board])

      if isValidSelection(board, current_player, old_x, old_y) == True:
        pass # Do nothing if player has made a valid selection
      else:
        continue # Looping indefintely until a valid choice has been selected by the current player

      while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
          game_over = True
        elif event.type == pygame.MOUSEBUTTONUP:
          new_pos = pygame.mouse.get_pos()
          # Translating mouse x, y screen coordinates to matrix coordinates
          new_x = (new_pos[0] // width)
          new_y = (new_pos[1] // height)
          # print(f"New coordinates: [{new_x}, {new_y}]")

          if board[old_y][old_x] == friendly['pawn']:
            if isValidMove(current_player, board, old_x, old_y, new_x, new_y) is True:
              board[new_y][new_x] = friendly['pawn']
              board[old_y][old_x] = empty

              if checkForWin(current_player, board) is True:
                game_over = True

              # If the total amount of chips has changed and a double
              # jump opportunity is available do not switch sides.
              current_piece_total = sum([sum(row) for row in board])

              if previous_piece_total > current_piece_total:
                  if checkIfDoubleJumpPossible(board, new_x, new_y) is True:
                    pass
                  else:
                      # Swap sides
                      if current_player == 1:
                        current_player = 2
                        print("Black.")
                      else:
                        current_player = 1
                        print("White.")

                      friendly, enemy = enemy, friendly
              else:
                # Swap sides
                if current_player == 1:
                  current_player = 2
                  print("Black.")
                else:
                  current_player = 1
                  print("White.")

                friendly, enemy = enemy, friendly

          if board[old_y][old_x] == (friendly['queen']):
            if isValidQueenMove(current_player, board, old_x, old_y, new_x, new_y) is True:

              if checkForWin(current_player, board) is True:
                game_over = True

              # If the total amount of pieces has changed and a double
              # jump opportunity is available do not switch sides.
              current_piece_total = sum([sum(row) for row in board])

              if previous_piece_total > current_piece_total:
                if checkIfDoubleJumpPossible(board, new_x, new_y) is True:
                  print(f"double jump is possible")
                  pass
                else:
                  if current_player == 1:
                    current_player = 2
                    print("Black.")
                  else:
                    current_player = 1
                    print("White.")

                  friendly, enemy = enemy, friendly
              else:
                if current_player == 1:
                  current_player = 2
                  print("Black.")
                else:
                  current_player = 1
                  print("White.")

                friendly, enemy = enemy, friendly


          # Turn player into queen if they make it to the opposite side of the board
          for row in range(8):
            for column in range(8):
              # Checking for player 1 queen pieces
              if board[0][column] == 1:
                board[0][column] = 3
                # Checking for player 2 queen pieces
              elif board[7][column] == 2:
                board[7][column] = 4
          break

  # Limit to 60 frames per second
  clock.tick(60)

  # Draw onto screen
  drawBoard(board)

  # Update screen
  pygame.display.flip()

# Exit the game
pygame.quit()