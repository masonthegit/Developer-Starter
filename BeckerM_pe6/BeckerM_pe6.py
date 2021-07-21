# Written by: Mason Becker
# PE: 13
import Turtle
from Turtle import drawChessboard

def main():
    startX, startY = eval(input("Enter starting coordinates (x, y): "))
    height = input("Enter height of chessboard: ")
    width = input("Enter width of chessboard: ")
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
    Turtle.done()
main()