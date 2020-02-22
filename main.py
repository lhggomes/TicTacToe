# PROJECT TIC TAC TOE

# Creating a Board for the Game 
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - ", ]
# Function to Display the board 
def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
# Let's play the game! 


def playGame():
    print("The Initial Game!")
    displayBoard()

while playingGame:
    handleTurn(currentPlayer)
    checkIfGameOver()
    flipPlayer()

#Defining a Function to Handle the Positons
def handleTurn():
    position = input("Choose a positon from 1-9: ")
    position = int(position) - 1
    board[position] = "X"
    displayBoard()
# Functions to Check the Status of the game
def checkIfGameOver():
    checkIfWin()
    checkIfTie()

#Checking if we have a winner for the Game
def checkIfWin():
    # Check Rows
    # Check Columns
    # Check Diagonals
    return

#Checking if we have an Tie! 
def checkIfTie():
    return
def flipPlayer(): 
    return 
playGame()
# check win
# check rows
# check columns
# check diagonals
