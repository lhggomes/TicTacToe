# PROJECT TIC TAC TOE

# Creating a Board for the Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# If Game Still going
playingGame = True
# Who on? Or there's a Tie?
winner = None
# Whos turn this it
currentPlayer = "X"

# Functions to check the status of the game


def checkForWinner():

    global winner
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonal()
    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner

    else:
        winner = None
    return


def checkRows():
    # Global Variables
    global playingGame
    # Checking THe Rows
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # If Rows are complete
    if row1 or row2 or row3:
        playingGame = False
    # Retunr the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def checkColumns():
    global playingGame
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        playingGame = False

    if column1:
        return board[0]
    elif column2:
        return board[3]
    elif column3:
        return board[6]

    return


def checkDiagonal():
    global playingGame

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        playingGame = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return


def checkIfTie():
    global playingGame
    if "-" not in board:
        playingGame = False
       

    return


def flipPlayer():
    global currentPlayer
    # Changing the current player between O and X
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

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
    board[position] = currentPlayer
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
