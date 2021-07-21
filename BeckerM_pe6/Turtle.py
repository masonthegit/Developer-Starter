import turtle

def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    drawRectangle(width, height)
    drawAllRectangles(startX, startY, width, height)

def drawAllRectangles(startX, startY, width=250, height=250):
    for i in range(1, 9):
        if i % 2 != 0:
            for j in range(0, 4):
                rectangleCornerX = startX + (width / 8) * j * 2
                rectangleCornerY = startY + (height / 8) * (i - 1)
                turtle.penup()
                turtle.goto(rectangleCornerX, rectangleCornerY)
                turtle.pendown()
                turtle.begin_fill()
                drawRectangle(width / 8, height / 8)
                turtle.end_fill()

        else:
            for j in range(0, 4):
                rectangleCornerX = startX + width / 8 + width / 8 * j * 2
                rectangleCornerY = startY + height / 8 * (i - 1)
                turtle.penup()
                turtle.goto(rectangleCornerX, rectangleCornerY)
                turtle.pendown()
                turtle.begin_fill()
                drawRectangle(width / 8, height / 8)
                turtle.end_fill()

def drawRectangle(width, height):
    turtle.setheading(0)
    turtle.speed(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

def done():
    turtle.done()