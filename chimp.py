from graphics import*
import time
import random
import math

def isReady(click):
    if click.getX() in range(350,550) and click.getY() in range(820,880):
        return True
    return False

def showLives(lives):
    global counter
    counter = Text(Point(200,850), "lives: " + str(lives))
    counter.setSize(30)
    counter.draw(wins)
def chimptest():
    global wins
    wins = GraphWin("Chimp Test", 900, 900)
    while True:
        lives = 3
        for i in range(1,30):
            showLives(lives)
            boxes = []
            labels = []
            rects = []
            s = 0
            rect1 = Rectangle(Point(350, 820), Point(550, 880))
            rect1.setFill("white")
            rect1.setOutline("black")
            rect1.draw(wins)
            label1 = Text(Point(450,850), "Ready")
            label1.setSize(30)
            label1.draw(wins)
            for j in range(i):
                while True:
                    s = random.randint(1,30)
                    if s not in boxes:
                        boxes.append(s)
                        break
                row = math.ceil((s/6))-1
                column = s % 6
                if (column == 0):
                    column = 6
                rect = Rectangle(Point((column-1)*150, row*150), Point(column*150, row*150+150))
                rect.setFill("white")
                rect.setOutline("black")
                rect.draw(wins)
                rects.append(rect)
                label = Text(Point(column*150-75,row*150+75), j+1)
                label.setSize(30)
                label.draw(wins)
                labels.append(label)
            while True:
                click = wins.getMouse()
                if isReady(click):
                    break
            rect1.undraw()
            label1.undraw()
            for label in labels:
                label.undraw()
            value = -1
            gameOver = False
            for j in range(i):
                while True:
                    click = wins.getMouse()
                    x = math.ceil(click.getX()/150)
                    y = math.ceil(click.getY()/150)
                    if (x < 7)  and (y < 6):
                        value = 6*y-6+x
                        if value in boxes:
                            break
                if boxes[j] != value:
                    gameOver = True
                    for x in range(j,len(rects)):
                        rects[x].undraw()
                    break
                else:
                    rects[j].undraw()
            if gameOver:
                lives -= 1
            counter.undraw()
            if (lives == 0):
                break
        showLives(lives)
        if not showChoices():
            break
        counter.undraw()
    wins.close()
def showChoices():
    rect2 = Rectangle(Point(175, 100), Point(400, 200))
    rect2.setFill("white")
    rect2.setOutline("black")
    rect2.draw(wins)
    rect1 = Rectangle(Point(500, 100), Point(725, 200))
    rect1.setFill("white")
    rect1.setOutline("black")
    rect1.draw(wins)
    label2 = Text(Point(287,150), "Restart")
    label2.setSize(30)
    label2.draw(wins)
    label1 = Text(Point(612,150), "Exit")
    label1.setSize(30)
    label1.draw(wins)
    while True:
        click = wins.getMouse()
        if click.getY() in range(100,200) and click.getX() in range(175,400):
            label1.undraw()
            label2.undraw()
            rect1.undraw()
            rect2.undraw()
            return True
        if click.getY() in range(100,200) and click.getX() in range(500,725):
            label1.undraw()
            label2.undraw()
            rect1.undraw()
            rect2.undraw()
            return False
        
    
