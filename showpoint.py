from graphics import *

win = GraphWin("My Window",900,900)
win.setBackground("black")
msg = Text(Point(100,100),"Hello!")
msg.setTextColor("red")
msg.draw(win)
#พิกัด แสดงตาม Mouse Click
while True:
    an=msg.getAnchor()
    p = win.getMouse()  
    x=p.x-an.x
    y=p.y-an.y
    msg.setText(p)
    msg.move(x,y)
    
    