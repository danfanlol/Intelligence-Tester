from graphics import*
import time
import random
import math

def showlives():
    global llabel
    llabel = Text(Point(500,50), "Lives: " + str(lives))
    llabel.setSize(30)
    llabel.draw(wins)
def visualMemory():
    global wins, lives
    wins = GraphWin("Visual Memory", 1000, 1000)
    wins.setBackground("white")
    while True:
        lives = 3
        i = 3
        while i <= 30:
            showlives()
            if lives == 0:
                break
            clear = []
            numboxes = math.floor(((i-3)/2)+3)
            factor = 800/numboxes
            y = 100
            for j in range(numboxes):
                x = 100
                for k in range(numboxes):
                    rect = Rectangle(Point(x, y), Point(x+factor, y+factor))
                    rect.setFill("white")
                    rect.setOutline("black")
                    rect.draw(wins)
                    clear.append(rect)
                    x += factor
                y += factor
            boxes = []
            rects = []
            for j in range(i):
                while True:
                    s = random.randint(1,numboxes*numboxes)
                    if s not in boxes:
                        boxes.append(s)
                        break
            for s in boxes:
                row = math.ceil((s/numboxes))-1
                column = s % numboxes
                if (column == 0):
                    column = numboxes
                rect = Rectangle(Point((column-1)*factor+100, row*factor+100), Point(column*factor+100, row*factor+factor+100))
                rect.setFill("yellow")
                rect.setOutline("black")
                rect.draw(wins)
                rects.append(rect)
            cur = time.time()
            while (True):
                if (time.time() - cur > 1.5):
                    break
            for rect in rects:
                rect.undraw()
            storage = []
            values = []
            wrong = 0
            wrongs = []
            wronglist = []
            while True:
                if len(boxes) == 0:
                    break
                if wrong == 3:
                    lives -= 1
                    break
                click = wins.getMouse()
                row = math.ceil((click.getX() - 100)/factor)
                column = math.ceil((click.getY()-100)/factor)
                value = numboxes*column-numboxes+row
                if value in range(1,numboxes*numboxes+1):
                    if value in boxes:
                        values.append(value)
                        rects[boxes.index(value)].draw(wins)
                        storage.append(rects[boxes.index(value)])
                        del rects[boxes.index(value)]
                        boxes.remove(value)
                    elif value not in values and value not in wronglist:
                        wronglist.append(value)
                        wrong += 1
                        rect = Rectangle(Point((row-1)*factor+100, (column-1)*factor+100), Point((row-1)*factor+100+factor, (column-1)*factor+factor+100))
                        rect.setFill("red")
                        rect.setOutline("black")
                        rect.draw(wins)
                        wrongs.append(rect)
            for d in wrongs:
                d.undraw()
            for d in clear:
                d.undraw()
            for rect in storage:
                rect.undraw()
            if wrong != 3:
                i += 1
            llabel.undraw()
        if not showChoices():
            break
        llabel.undraw()
    wins.close()
            
    
def showChoices():
    rect = Rectangle(Point(100, 300), Point(400, 400))
    rect.setFill("white")
    rect.setOutline("black")
    rect.draw(wins)
    rect1 = Rectangle(Point(600, 300), Point(900, 400))
    rect1.setFill("white")
    rect1.setOutline("black")
    rect1.draw(wins)
    label1 = Text(Point(250,350), "Restart")
    label1.setSize(30)
    label1.draw(wins)
    label2 = Text(Point(750,350), "Exit")
    label2.setSize(30)
    label2.draw(wins)
    while True:
        click = wins.getMouse()
        click.getX()
        if click.getX() in range(100,400) and click.getY() in range(300,400):
            rect.undraw()
            rect1.undraw()
            label1.undraw()
            label2.undraw()
            return True
        if click.getX() in range(600,900) and click.getY() in range(300,400):
            rect.undraw()
            rect1.undraw()
            label1.undraw()
            label2.undraw()
            return False
