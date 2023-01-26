from graphics import *

win = GraphWin("My Window",400,400)
t=0.001

for x in range(33,256):
    win.setBackground(color_rgb(255,x,0))
    time.sleep(t)

for x in range(33,256):
    win.setBackground(color_rgb(255-x,255,0))
    time.sleep(t)

for x in range(33,256):
    win.setBackground(color_rgb(33,255,x))
    time.sleep(t)

for x in range(33,256):
    win.setBackground(color_rgb(33,255-x,255))
    time.sleep(t)
    
for x in range(33,256):
    win.setBackground(color_rgb(x,33,255))
    time.sleep(t)

for x in range(33,256):
    win.setBackground(color_rgb(255,33,255-x))
    time.sleep(t)

win.getKey()


