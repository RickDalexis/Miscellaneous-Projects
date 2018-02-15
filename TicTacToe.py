import random

win = False
#this is the array that hold the values that will be inserted into the board
board =  [" "," "," ",
          " "," "," ",
         " "," "," "]
WhoseTurn = "n"

def  checkSpace(position):
    return board[position]== " "


def drawBoard(place,letter):

    #board[int(place)-1] = letter
    board[int(place)] = letter
    #board.insert(int(place)-1,letter)
    print(" %s | %s | %s" % (board[0],board[1],board[2]))
    print("-----------")
    print(" %s | %s | %s" % (board[3], board[4], board[5]))
    print("-----------")
    print(" %s | %s | %s" % (board[6], board[7], board[8]))

def instructions():
    print("Welcome to Tic-Tac-Toe!!")
    print("You do all this shit yeah!!")

def whoGoesFirst():
    global WhoseTurn
    player_guess = random.randint(1,10)
    computer_guess = random.randint(1, 10)
    print("Randomly Choosing who goes First")
    if player_guess>computer_guess:
        print("The human gets to go first")
        WhoseTurn = "Human"
    else:
        print("Ha I get to go first")
        WhoseTurn = "Computer"

def Winner(letter):
    return( (board[0] == letter and board[1] == letter and board[2] == letter) or  #The first three cover winning by row
            (board[3] == letter and board[4] == letter and board[5]) or
            (board[6] == letter and board[7] == letter and board[8] == letter) or
            #The next three cover winning by column
            (board[0] == letter and board[3] == letter and board[6] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter)
            )
def getPlayerMove():
    global WhoseTurn
    move = input("Where would you like to go?")
    if checkSpace(int(move)):
        drawBoard(move, "X")
        if Winner("X"):
            print("You won!!")

        else:
            WhoseTurn = "Computer"
    else:
        print("You entered an invalid statment")
    #WhoseTurn = "Computer"
def getComputerMove():
    global WhoseTurn
    move = random.randint(0, 8)
    if checkSpace(move):
        drawBoard(move, "O")
    else:
        getComputerMove()
    WhoseTurn = "Human"


instructions()
whoGoesFirst()
drawBoard(-1," ")


while win == False:
    if WhoseTurn=="Human":
        getPlayerMove()
        if Winner("X"):
            print("YaY")
    elif (WhoseTurn == "Computer"):
       print("It is the computer's turn")
       getComputerMove()
       Winner("O")




