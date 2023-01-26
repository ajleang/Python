from graphics import *

win = GraphWin("My Window",900,900)
win.setBackground("black")
msg = Text(Point(100,100),"Hello!")
msg.setTextColor("red")
msg.draw(win)
while True:
    p = win.getKey()
    msg.setText(p)
    
    