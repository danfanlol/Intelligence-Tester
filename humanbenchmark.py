from graphics import*
import time
import random
import math
import number, sequence, verbal, chimp, visual
def setup():
    global win
    win = GraphWin("Human Intelligence Benchmark", 1200, 1200)
    win.setBackground("white")
def drawChoices(win):
    choices = ["Sequence Memory", "Number Memory", "Verbal Memory", "Chimp Test", "Visual Memory"]
    iy = 100
    for i in range(2):
        ix = 100
        y = iy
        for j in range(2):
            x = ix
            ix += 500
            rect = Rectangle(Point(x, y), Point(x+400, y+200))
            rect.setFill("white")
            rect.setOutline("black")
            rect.draw(win)
            label = Text(Point(x+200, y+100), choices[2*i+j])
            label.setSize(30)
            label.draw(win)
        iy += 250
    rect = Rectangle(Point(100, 600), Point(1000, 800))
    rect.setFill("white")
    rect.setOutline("black")
    rect.draw(win)
    label = Text(Point(550,700), "Visual Memory")
    label.setSize(30)
    label.draw(win)
    rect = Rectangle(Point(400, 850), Point(700, 950))
    rect.setFill("white")
    rect.setOutline("black")
    rect.draw(win)
    label = Text(Point(550,900), "Exit")
    label.setSize(30)
    label.draw(win)
    
def getBox(click):
    iy = 100
    for i in range(2):
        ix = 100
        y = iy
        for j in range(2):
            x = ix
            ix += 500
            if click.getX() in range(x,x+400) and click.getY() in range(y,y+200):
                return 2*i+j
        iy += 250
    if click.getX() in range(100,1000) and click.getY() in range(600,800):
        return 4
    if click.getX() in range(400,700) and click.getY() in range(850,950):
        return 5
    return -1

def main():
    setup()
    drawChoices(win)
    over = False
    while not over:
        click = win.getMouse()
        num = getBox(click)
        if num == 0:
            sequence.sequencememory()
        if num == 1:
            number.numbermemory()
        if num == 2:
            verbal.verbalmemory()
        if num == 3:
            chimp.chimptest()
        if num == 4:
            visual.visualMemory()
        if num == 5:
            break
    win.close()
    
        
main()
    
