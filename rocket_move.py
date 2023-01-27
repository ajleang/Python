from graphics import *

win = GraphWin("My Window", 900, 900)
win.setBackground("black")

rocket_u = Image(Point(100, 100), "rocket_u.gif")
rocket_d = Image(Point(100, 100), "rocket_d.gif")
rocket_l = Image(Point(100, 100), "rocket_l.gif")
rocket_r = Image(Point(100, 100), "rocket_r.gif")
rocket_u.draw(win)


def r_move(x, y, dir):
    rocket_u.move(x, y)
    rocket_d.move(x, y)
    rocket_l.move(x, y)
    rocket_r.move(x, y)
    rocket_u.undraw()
    rocket_d.undraw()
    rocket_l.undraw()
    rocket_r.undraw()

    if dir == "Up":
        rocket_u.draw(win)
    if dir == "Down":
        rocket_d.draw(win)
    if dir == "Left":
        rocket_l.draw(win)
    if dir == "Right":
        rocket_r.draw(win)

while True:
    d = win.getKey()
    if d == "Up":
        r_move(0, -10, d)
    if d == "Down":
        r_move(0, 10, d)
    if d == "Right":
        r_move(10, 0, d)
    if d == "Left":
        r_move(-10, 0, d)


win.getKey()
