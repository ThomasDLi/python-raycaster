import turtle
import math

t = turtle.Turtle()
t.right(90)
t.speed(0)
t.pensize(50)
walls = [
    ((1, 1), (1, 5)),
    ((2, 2), (5, 5))
]

def line_intersection(line12, line22):

    #find slope
    line1 = line12
    line2 = line22

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    #find intersection

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    #calculate offset

    div = det(xdiff, ydiff)

    #return if lines don't touch, so it doesn't 0dvisErr

    if div == 0:
       return 0, 0

    #return calculated values

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

view = 1
coord = [0, 0]
raycoord = [0, 0]
dist = 10000
display = [0] * 100
linec = 0

while(True):

    inp = input()
    if(inp == "a"):
        view -= 40
    if(inp == "d"):
        view += 40
    if(inp == "s"):
        coord[0] += 1
    if(inp == "w"):
        coord[0] -= 1

    if(inp == "j"):
        coord[1] += 1
    if(inp == "l"):
        coord[1] -= 1

    t.clear()

    h = 0

    for x in range(100):

        b = x + view

        #convert b (angle) into m (slope)

        m = math.tan(b)

        #project forward
    
        dx = dist / math.sqrt(1 + (m * m))
        dy = m * dx

        #adjust it to player coords

        newx = coord[0] + dx
        newy = coord[1] + dy

        #find where ray meets wall

        lineint = line_intersection(walls[h], ((newx, newy), coord))

        #dist = math.hypot(coord[0] - lineint[0], coord[1] - lineint[1])

        dist = math.sqrt((coord[0] - lineint[0])**2 + (coord[1] - lineint[1])**2)

        display[x] = dist

        if(lineint != None and display[x] > 10):
            t.penup()
            t.goto(x * 3, display[x] / 2)
            t.pendown()
            t.forward(display[x])

    print(display)
