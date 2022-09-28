import turtle
from INPUTS import WIDTH, HEIGHT, SQUARE_SIZE, MAZE, START, END
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

        #Wall?
        try: #No better way to check if index exists in dictionary?
            if MAZE[x][y]: square.toggleWall()
        except KeyError: pass
pen.up()

#Attempt to solve
#From the end, go back along the path with the least weight
def tracebackSquare(square):
    leastWeight = square.weight
    leastWeightSquare = None

    for o in [square.up(), square.down(), square.left(), square.right()]:
        if o:
            if o.weight != 0 and o.weight < leastWeight:
                leastWeight = o.weight
                leastWeightSquare = o

    if leastWeightSquare is None:
        print("SOLVED!", square.x, square.y)
    else:
        leastWeightSquare.makePath()
        leastWeightSquare.writeWeight() #So it doesn't get coloured over
        tracebackSquare(leastWeightSquare)

#From the start, go to each surrounding square incrementing weight by 1 each move
def numberSquare(square, weight=1):
    if square:
        if square.weight == 0:
            if not square.isWall:
                square.weight = weight
                square.writeWeight()

                if not (square.x == END[0] and square.y == END[1]):
                    numberSquare(square.up(), weight+1)
                    numberSquare(square.down(), weight+1)
                    numberSquare(square.left(), weight+1)
                    numberSquare(square.right(), weight+1)
                else:
                    #Reached the end square. Begin traceback
                    square.makePath()
                    square.writeWeight()
                    tracebackSquare(square)


startSquare = squares[START[0]][START[1]]
numberSquare(startSquare)


#Render screen
turtle.done()