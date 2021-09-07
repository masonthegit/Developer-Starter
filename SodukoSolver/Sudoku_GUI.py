# This program creates a random Sudoku board GUI using Python 3
#! /usr/bin/env/python3

# You will need to install pygame to run this program
# To install pygame type "pip3 install pygame" in the terminal

# Instructions:
# Clicking on an empty square lets you select it
# After selecting a square you can enter a number from 1-9
# You can enter numbers as many times as you like, but once you press enter, the number will be locked into place
# If you enter a number that is in the same cube, row, or column as the same number, it will be rejected instead
# If you enter a number that will force another square into the same situation, it will still be rejected
# To win you must fill the board with numbers that are all locked into place using the same rules as Sudoku

import pygame
from Sudoku_Solver import solve, valid
import time
import random
pygame.font.init()

class Grid:
# The First Sudoku Board
    board1 = [
        [2,0,0,0,0,6,5,7,0],
        [4,9,0,0,2,7,0,0,1],
        [0,0,0,0,0,0,2,0,3],
        [5,4,0,0,7,3,0,9,0],
        [7,0,6,0,0,0,3,0,4],
        [0,8,0,2,6,0,0,1,5],
        [6,0,9,0,0,0,0,0,0],
        [8,0,0,9,4,0,0,3,6],
        [0,1,4,6,0,0,0,0,7]
    ]

# The Second Sudoku Board
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

# The Third Sudoku Board
    board3 = [
        [0,0,0,0,1,0,0,0,9],
        [9,1,8,0,0,4,0,0,0],
        [4,0,7,0,0,0,5,0,1],
        [0,0,0,2,6,0,9,7,4],
        [0,0,0,1,0,0,3,0,2],
        [0,0,0,4,0,0,1,5,0],
        [0,0,4,0,5,6,2,0,8],
        [0,0,0,0,3,0,0,1,0],
        [2,5,0,0,0,1,6,9,7]
    ]

# Randomly Picks A Sudoku Board
    board_list = [board1, board2, board3]
    board = random.choice(board_list)

# The Basic Values For Board Class
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

# Updates The Board
    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

# Makes The Temporary Value A Permanent Value If Valid
    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

# Adds The Temporary Number Value You Input
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

# Draw Grid Lines
    def draw(self, win):
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

# Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

# Selects The Square You Clicked On
    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

# Clears Temporary Values
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

# Returns The Position Of Where You Clicked On The GUI
    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

# Checks If The Board Is Filled
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

# Class That Creates The Cubes
class Cube:
    rows = 9
    cols = 9

# Basic Values For Cube Class
    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

# Draws The GUI
    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

# Basic Values For Draw
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

# Color Of Temporary Number
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (0, 0, 0))
            win.blit(text, (x+5, y+5))

# Color Of Permanent Value
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

# Color Of Selected Square
        if self.selected:
            pygame.draw.rect(win, (150, 255, 0), (x,y, gap ,gap), 3)

# Defines Values For Temporary And Permanent
    def set(self, val):
        self.value = val
    def set_temp(self, val):
        self.temp = val

# Update Window
def redraw_window(win, board, time, strikes):
    win.fill((102, 51, 0))

# Draw Time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 200, 560))

# Draw Strikes
    scoretext = fnt.render("Mistakes: {0}".format(strikes), 1, (0, 0, 0))
    win.blit(scoretext, (20, 560))

# Draw Grid and Board
    board.draw(win)

# Sets The Values For Time
def format_time(secs):
    sec = secs % 60
    minute = secs // 60 
    hour = minute // 60

# Formats The Time
    mat = "{:01d}:{:02d}:{:02d}".format(hour, minute, sec)
    return mat

# Main Function For The Program
def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        play_time = round(time.time() - start)

# Quits The Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

# Keys For Number Input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

# Deletes Temporary Number Value
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

# Enters Number Value As Permanent Value If Valid
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Correct")
                        else:
                            print("Incorrect")
                            strikes += 1
                        key = None

# Messages For Solving The Board Based On Strike Count
                        if board.is_finished():
                            print("You Win")
                            if strikes == 0:
                                print("You Did Perfect!")
                            elif strikes > 0 and strikes <= 10:
                                print("Great Job!")
                            elif strikes > 10 and strikes <= 30:
                                print("You Did Good")
                            elif strikes > 30:
                                print("Can You Do Better?")
                            run = False

# Gets The Position On The GUI You Clicked On
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

# Redraws The GUI Based On Any Changes On Values
        redraw_window(win, board, play_time, strikes)
        pygame.display.update()

# Runs The Program
main()
pygame.quit()