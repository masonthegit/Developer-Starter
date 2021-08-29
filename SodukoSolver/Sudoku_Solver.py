# Uses back tracking to solve the board
def solve(bo):

# Checks if the board if filled
    find = find_zero(bo)
    if not find:
        return True
    else:
        row, col = find
    
# Loops through the numbers 1-9 to fill a space
    for i in range(1, 10):

        # Only adds value if it is valid
        if valid(bo, i, (row, col)):
            bo[row][col] = i
        
# Try to solve
            if solve(bo):
                return True
            
# Backtracks a false value
            bo[row][col] = 0
    
# Marks a space as false
    return False

# Checks if the board follows the rules of Sudoku
def valid(bo, num, pos):

# Checks a row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
# Checks a column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
# Checks a 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

# Locates a given 3x3 box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
# Marks the box as valid
    return True

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
                print(str(bo[i][j]) + " ", end = "")

# Finds a zero/empty space
def find_zero(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):

# Checks for zero
            if bo[i][j] == 0:
                return(i, j) # i = row, j = column
    
# Marks the board as filled
    return None