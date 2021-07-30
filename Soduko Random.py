import random

# This program creates a random Sudoku board in text

# The first Sudoku board
board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# The second Sudoku board
board2 = [
    [0,0,0,0,0,0,0,0,9],
    [0,8,0,0,6,3,0,4,7],
    [0,0,0,1,2,5,6,0,0],
    [9,3,8,6,0,4,7,1,0],
    [0,7,0,3,0,0,0,6,0],
    [0,0,1,2,0,7,4,0,0],
    [0,0,0,0,0,2,0,0,0],
    [0,5,7,0,9,0,0,2,4],
    [4,0,2,0,0,0,0,0,0]
]

board_list = [board1, board2]

board = random.choice(board_list)

# Divides the board into 3x3 boxes
def print_board(bo):
    for i in range(len(bo)):

# Divides the board into rows of three
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

# Divides the board into columns of three
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

# Fills in the board with numbers
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# Prints the random board
print_board(board)