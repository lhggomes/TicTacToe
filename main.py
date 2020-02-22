# PROJECT TIC TAC TOE 

# board
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - ", ]
# display

def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# play game
def playGame():
    # Display the board for the begining of the game
    displayBoard()
    handleTurn()

# Handles turn
def handleTurn():
    position = input("Choose a positon from 1-9: ")

 
playGame()
# check win
    # check rows
    # check columns
    # check diagonals
# check tie

# flip player
