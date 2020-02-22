# PROJECT TIC TAC TOE

# GLOBAL VARIABLES

# Creating a Board for the Game
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - ", ]
# If Game Still going
playingGame = True

# Who on? Or there's a Tie?
winner = None

# Whos turn this it
currentPlayer = "X"

# Function to Display the board


def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
# Let's play the game!


def playGame():
    print("The Initial Game!")
    displayBoard()

# Defining a Function to Handle the Positons
def handleTurn(currentPlayer):
    position = input("Choose a positon from 1-9: ")
    position = int(position) - 1
    board[position] = "X"
    displayBoard()
# While the game still going
while playingGame:
    # Handlgin the turn of players
    handleTurn(currentPlayer)
    # Check if the game has ended
    checkIfGameOver()

    # Flip to the other player
    flipPlayer()
    # The Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")
# Functions to Check the Status of the game


def checkIfGameOver():
    checkIfWin()
    checkIfTie()
# Checking if we have a winner for the Game


def checkIfWin():
    # Check Rows
    # Check Columns
    # Check Diagonals
    return
# Checking if we have an Tie!


def checkIfTie():
    return


def flipPlayer():
    return


playGame()
# check win
# check rows
# check columns
# check diagonals
