# PROJECT TIC TAC TOE

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

# Functions to check the status of the game


def checkForWinner():
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonal()
    return


def checkRows():
    return


def checkColumns():
    return


def checkDiagonal():
    return


def checkIfTie():
    return


def flipPlayer():
    return


def checkIfGameOver():
    checkForWinner()
    checkIfTie()


# Display the Board
def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Let's play the game!
displayBoard()


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

    flipPlayer()
    # The Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")
