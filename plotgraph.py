import math
from graphics import *

win = GraphWin("My Window",900,900)
win.setBackground("black")
win.setCoords(0,-450,900,450)
for x in range(0,900,1):
    y=math.sin(x/50)*200
    win.plot(x,y,"white")    
    print(x,y)
    time.sleep(.001)

win.getKey()