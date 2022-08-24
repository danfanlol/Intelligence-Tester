from graphics import*
import time
import random
import math

def numberconsole():
    for i in range(10):
        rect = Rectangle(Point(i*80, 750), Point(80*(i+1), 800))
        rect.setFill("light blue")
        rect.setOutline("black")
        rect.draw(wind)
        label = Text(Point(80*i+40,775), i)
        label.setSize(20)
        label.draw(wind)
def createNumber(length):
    s = ''
    for i in range(length):
        d = random.randint(0,9)
        if (d == 0 and i == 0 and length != 1):
            d = random.randint(1,9)
        s += str(d)
    return s
def displayNumber(number, timeleft):
    global label3, label4, rect, label5, label8, label9
    label = Text(Point(400,200), number)
    label.setSize(20)
    label.draw(wind)
    s = time.time()
    label2 = Text(Point(400,500), timeleft)
    label2.setSize(20)
    label2.draw(wind)
    while (timeleft != 0):
        if (time.time() - s >= 1):
            s = time.time()
            timeleft -= 1
            label2.undraw()
            label2 = Text(Point(400,500), timeleft)
            label2.setSize(20)
            label2.draw(wind)
    label2.undraw()
    label.undraw()
    label3 = Text(Point(400,200), "What is the number?")
    label3.setSize(20)
    label3.draw(wind)
    rect = Rectangle(Point(350, 600), Point(450, 650))
    rect.setFill("light blue")
    rect.setOutline("black")
    rect.draw(wind)
    label5 = Text(Point(400,625), "Submit")
    label5.setSize(20)
    label5.draw(wind)
    userres = ""
    label4 = Text(Point(400,400), userres)
    label4.setSize(20)
    label4.draw(wind)
    while True:
        click = wind.getMouse()
        number1 = getNumberBox(click)
        if number1 >= 0:
            label4.undraw()
            userres += str(number1)
            label4 = Text(Point(400,400), userres)
            label4.setSize(20)
            label4.draw(wind)
        if number1 == -2:
            break
    if int(userres) == int(number):
        return True
    label8 = Text(Point(400,400), "Real answer: " + number)
    label8.setSize(20)
    label8.draw(wind)
    label9 = Text(Point(400,600), "Your guess: " + userres)
    label9.setSize(20)
    label9.draw(wind)
    return False
            
def getNumberBox(click):
    number = -1
    if click.getY() in range(750,800):
        number = math.floor(click.getX()/80)
    elif click.getY() in range(600,650):
        if click.getX() in range(350,450):
            number = -2
    return number

def displayError():
    global re, rel, rect2, exl
    re = Rectangle(Point(250, 50), Point(350, 100))
    re.setFill("light blue")
    re.setOutline("black")
    re.draw(wind)
    rel= Text(Point(300,75), "Restart")
    rel.setSize(20)
    rel.draw(wind)
    rect2 = Rectangle(Point(450, 50), Point(550, 100))
    rect2.setFill("light blue")
    rect2.setOutline("black")
    rect2.draw(wind)
    exl= Text(Point(500,75), "Exit")
    exl.setSize(20)
    exl.draw(wind)
def numbermemory():
    global wind
    wind = GraphWin("number memory", 800, 800)
    numberconsole()
    over = False
    while True:
        length = 1
        time = 3
        while True:
            number = createNumber(length)
            if displayNumber(number, time):
                length += 1
                time += 1
                label3.undraw()
                label4.undraw()
                label5.undraw()
                rect.undraw()
            else:
                label3.undraw()
                label4.undraw()
                label5.undraw()
                rect.undraw()
                displayError()
                break
        while True:
            click = wind.getMouse()
            if click.getY() in range(50,100):
                if click.getX() in range(250,350):
                    re.undraw()
                    rel.undraw()
                    rect2.undraw()
                    exl.undraw()
                    label8.undraw()
                    label9.undraw()
                    break
                elif click.getX() in range(450,550):
                    over = True
                    break
        if over:
            break
    if over:
        wind.close()
    
