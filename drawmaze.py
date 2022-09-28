import turtle
from INPUTS import WIDTH, HEIGHT, SQUARE_SIZE
from utils.square import Square

turtle.tracer(0, 0)  # Stop screen refreshes

#Screen + pen
screen = turtle.getscreen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
pen = turtle.Turtle()

#Draw grid
squares = {}
for x in range(WIDTH):
    squares[x] = {}
    for y in range(HEIGHT):
        square = Square(pen, squares, x, y, SQUARE_SIZE)
        squares[x][y] = square

        #Drawing maze-making guidelines
        if x%2==1 and y%2==1:
            square.makePath() #Permenant walls
        if x%2==1 or y%2==1:
            square.toggleWall() #Removeable walls
pen.up()

#Draw maze
mazedata = {}
for X in range(WIDTH): mazedata[X] = {}

def onclick(x,y):
    try: #Attempt to locate a grid and toggle its wall
        squares[x//SQUARE_SIZE][y//SQUARE_SIZE].toggleWall()
    except KeyError: #User must've clicked outside of grid. -> this triggers export of maze
        export = {}
        for X in squares:
            export[X] = {}
            for Y in squares[X]:
                square = squares[X][Y]
                if square.isPath or square.isWall:
                    export[X][Y] = True
        print(export)

    turtle.update()
turtle.onscreenclick(onclick)

#Render screen
turtle.done()