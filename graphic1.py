from graphics import *

win = GraphWin("My Window",800,800)
win.setBackground(color_rgb(222,48,187))
win.setCoords(0,0,800,800)
for x in range(150):
    c = Circle(Point(100,x), 30)
    c.setFill(color_rgb(60,80,12))
    c.draw(win)
    time.sleep(.04)
    c.undraw()

#win.getMouse()