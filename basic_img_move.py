from graphics import *

win = GraphWin("My Window", 900, 900)
win.setBackground("black")


rocket_u = Image(Point(100, 100), "r.gif")
rocket_u.draw(win)

while True:
    d = win.getKey()
    if d == "Up":
        rocket_u.move(0, -10)
    if d == "Down":
        rocket_u.move(0, 10)
    if d == "Right":
        rocket_u.move(10, 0)
    if d == "Left":
        rocket_u.move(-10, 0)


win.getKey()
