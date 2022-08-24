from graphics import*
import time
import random
import math


def showboard():
    rect = Rectangle(Point(300, 800), Point(500, 900))
    rect.setOutline("black")
    rect.draw(winq)
    rect = Rectangle(Point(700, 800), Point(900, 900))
    rect.setOutline("black")
    rect.draw(winq)
    label3 = Text(Point(400, 850), "Seen")
    label3.setSize(30)
    label3.draw(winq)
    label3 = Text(Point(800, 850), "New")
    label3.setSize(30)
    label3.draw(winq)
def showscore(lives,score):
    global label, label2
    label = Text(Point(400, 300), "lives: " + str(lives))
    label.setSize(30)
    label.draw(winq)
    label2 = Text(Point(800, 300), "score: " + str(score))
    label2.setSize(30)
    label2.draw(winq)
def verbalmemory():
    global winq
    fin = open("s.txt")
    n = fin.readline().strip()
    winq = GraphWin("Verbal Memory", 1200, 1200)
    while True:
        current = []
        lives =3
        score = 0
        showboard()
        while True:
            showscore(lives,score)
            word = ""
            randomnumber = random.randint(1,3)
            if randomnumber == 1 and len(current) != 0:
                word = current[random.randint(0,len(current)-1)]
            else:
                word = n
                n = fin.readline().strip()
            label3 = Text(Point(600, 550), word)
            label3.setSize(30)
            label3.draw(winq)
            while True:
                click = winq.getMouse()
                if checkwordBox(click) == 1:
                    if word not in current:
                        lives -= 1
                    else:
                        score += 1
                    break
                elif checkwordBox(click) == 2:
                    if word in current:
                        lives -= 1
                    else:
                        score += 1
                    break
            if randomnumber != 1:
                current.append(word)
            label3.undraw()
            label.undraw()
            label2.undraw()
            if lives == 0:
                break
        showscore(lives,score)
        if showloss() == 2:
            break
        label.undraw()
        label2.undraw()
    fin.close()
    winq.close()
def showloss():
    rect = Rectangle(Point(700, 100), Point(900, 200))
    rect.setOutline("black")
    rect.draw(winq)
    rect2 = Rectangle(Point(300, 100), Point(500, 200))
    rect2.setOutline("black")
    rect2.draw(winq)
    label4 = Text(Point(800, 150), "Exit")
    label4.setSize(30)
    label4.draw(winq)
    label5 = Text(Point(400, 150), "Restart")
    label5.setSize(30)
    label5.draw(winq)
    while True:
        click = winq.getMouse()
        if (click.getY() in range(100,200) and click.getX() in range(700,900)):
            return 2
        if (click.getY() in range(100,200) and click.getX() in range(300,500)):
            return 1
        
            
def checkwordBox(click):
    if click.getY() in range(800,900) and click.getX() in range(300,500):
        return 1
    elif click.getY() in range(800,900) and click.getX() in range(700,900):
        return 2
    return 3
