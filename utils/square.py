import math

from INPUTS import WIDTH, HEIGHT, SQUARE_SIZE

def drawSquare(pen, x, y, size):
    pen.up()
    pen.goto(x * size, y * size)
    pen.down()
    pen.setheading(0)

    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
def fillSquare(pen, x, y, size, colour):
    pen.fillcolor(colour)
    pen.begin_fill()
    drawSquare(pen, x, y, size)
    pen.end_fill()
    pen.up()

class Square:
    def __init__(self, pen, squares, x, y, size):
        self.squares = squares
        self.size = size
        self.pen = pen
        self.x = x
        self.y = y

        self.isWall = False
        self.isPath = False
        self.weight = 0

        # Draw square
        drawSquare(pen, x, y, size)

    def goto(self):
        self.pen.goto(self.x*self.size, self.y*self.size)
        self.pen.setheading(0)

    def toggleWall(self):
        if self.isPath: return #For drawing maze
        self.isWall = not self.isWall
        fillSquare(self.pen, self.x, self.y, self.size, "black" if self.isWall else "white")

    def makePath(self):
        fillSquare(self.pen, self.x, self.y, self.size, "green")
        self.isPath = True

    def writeWeight(self):
        self.goto()
        self.pen.write(str(self.weight))

    def up(self):
        if self.y < HEIGHT-1: return self.squares[self.x][self.y+1]
    def down(self):
        if self.y > 0: return self.squares[self.x][self.y-1]
    def right(self):
        if self.x < WIDTH-1: return self.squares[self.x+1][self.y]
    def left(self):
        if self.x > 0: return self.squares[self.x-1][self.y]