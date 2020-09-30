import random
import os

displayBoard = []
hiddenBoard = []
found = 0
hidden = 0


def displayTopLine():
    print("  A B C D")

def displayRows():
    for x in range(4):
            row = displayBoard[x][0] + " " + displayBoard[x][1] + " " + displayBoard[x][2] + " " + displayBoard[x][3]
            print(str(x + 1) + " " + row)

def createBoardToDisplay():
    
    for x in range(4):
        row = []
        for y in range(4):
            row.append("O")
        displayBoard.append(row)

def createHiddenBoard():
    
    for x in range(4):
        row = []
        for y in range(4):
            row.append("O")
        hiddenBoard.append(row)

    for i in range(4):
        x = random.randint(0,3)
        y = random.randint(0,3)
        if (not hiddenBoard[x][y] == "X"):
            hiddenBoard[x][y] = "X"
            global hidden
            hidden += 1


def askForInput():
    correctInput = False
    while not correctInput:
        coords  = input("Please input coords in the format 'A1':")
        y = coords[0]
        x = int(coords[1])
        if (y in ["A","B","C","D"] and x >0 and x < 5):
            correctInput = True

    return coords

def hasWon(coords):
    y = coords[0]
    x = int(coords[1])-1

    if (y=="A"):
        y = 0
    if (y=="B"):
        y = 1
    if (y=="C"):
        y = 2
    if (y=="D"):
        y = 3


    if hiddenBoard[x][y] == "X":
        global found
        found += 1
        hiddenBoard[x][y] = "O"
        displayBoard[x][y] = "X"


def playGame():
    win = False
    createBoardToDisplay()
    createHiddenBoard()
    while not win:
        showTheBoard()
        coords = askForInput()
        win = hasWon(coords)
        showTheBoard()
        if found == 4:
            win = True
            print("You found them all")



def showTheBoard():
    os.system('clear')
    displayTopLine()
    displayRows()





playGame()