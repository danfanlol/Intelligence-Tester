from graphics import*
import time
import random
import math
def drawSequenceBoard():
    global arrays
    y = 200
    arrays = []
    for i in range(3):
        arrays.append([])
        x = 200
        for j in range(3):
            rect = Rectangle(Point(x, y), Point(x+200, y+200))
            rect.setFill("white")
            rect.setOutline("black")
            rect.draw(wins)
            arrays[i].append(rect)
            x += 200
        y += 200
def sequenceGetBox(click):
    y = 200
    for i in range(3):
        x = 200
        for j in range(3):
            if (click.getX() in range(x, x + 200) and click.getY() in range(y,y+200)):
                return 3*i + j
            x += 200
        y += 200
    return -1
def sequencePlay(steps, sequence):
    global ga
    for i in sequence:
        number = i
        col = number % 3
        row = math.floor(number/3)
        arrays[row][col].setFill("yellow")
        s = time.time()
        while (True):
            if (time.time() - s > .8):
                s = time.time()
                break
        arrays[row][col].setFill("white")
        while (True):
            if (time.time() - s > .2):
                break
    number = random.randint(0,8)
    sequence.append(number)
    col = number % 3
    row = math.floor(number/3)
    arrays[row][col].setFill("yellow")
    s = time.time()
    while (True):
        if (time.time() - s > .8):
            s = time.time()
            break
    arrays[row][col].setFill("white")
    while (True):
        if (time.time() - s > .15):
            break
    success = True
    for i in range(steps):
        while True:
            click = wins.getMouse()
            res = sequenceGetBox(click)
            if res >= 0:
                col = res % 3
                row = math.floor(res/3)
                arrays[row][col].setFill("red")
                if sequence[i] != res:
                    success = False
                else:
                    b = time.time()
                    while True:
                        if (time.time() - b > .1):
                            arrays[row][col].setFill("white")
                            break
                break
        if not success:
            ga = Text(Point(500, 150), "GAME OVER")
            ga.setSize(30)
            ga.draw(wins)
            return False
    return True
                
        
            
def sequenceExitButton():
    global res, ex, b1,b2
    res = Rectangle(Point(250, 50), Point(430, 100))
    res.setFill("light blue")
    res.setOutline("black")
    res.draw(wins)
    b1 = Text(Point(340, 75), "Restart")
    b1.setSize(30)
    b1.draw(wins)
    ex = Rectangle(Point(570, 50), Point(750, 100))
    ex.setFill("light blue")
    ex.setOutline("black")
    ex.draw(wins)
    b2 = Text(Point(660, 75), "Exit")
    b2.setSize(30)
    b2.draw(wins)
def sequencememory():
    global wins, grid
    wins = GraphWin("sequence", 1000, 800)
    wins.setBackground("white")
    rect = Rectangle(Point(200, 200), Point(400, 400))
    rect.setFill("white")
    rect.setOutline("black")
    rect.draw(wins)
    drawSequenceBoard()
    gameover = False
    while True:
        steps = 0
        sequence= []
        while True:
            steps += 1
            if (not sequencePlay(steps,sequence)):
                break
        sequenceExitButton()
        while True:
            click = wins.getMouse()
            if (click.getX() in range(250,430) and click.getY() in range(50,100)):
                ga.undraw()
                res.undraw()
                ex.undraw()
                b1.undraw()
                b2.undraw()
                for i in range(3):
                    for j in range(3):
                        arrays[i][j].setFill("white")
                break
            elif (click.getX() in range(570,750) and click.getY() in range(50,100)):
                gameover = True
                break
        if gameover:
            break
    wins.close()
