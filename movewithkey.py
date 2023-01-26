from graphics import *

win = GraphWin("My Window",900,900)
win.setBackground("black")
msg = Text(Point(100,100),"Hello!")
msg.setTextColor("red")
msg.draw(win)
while True:
    p = win.getKey()
    msg.setText(p)
    if p=="Up":
        msg.move(0,-10)
    if p=="Down":
        msg.move(0,10)
    if p=="Right":
        msg.move(10,0)
    if p=="Left":
        msg.move(-10,0)
    