import turtle as trt
import math

trt.tracer(0)


def rotate_point(p, angle, center):
    rad = math.radians(angle)
    x, y = p
    cx, cy = center
    xr = cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad)
    yr = cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad)
    return xr, yr


def triangle(x, y, z, color):
    trt.penup()
    trt.goto(x)
    trt.pendown()
    trt.fillcolor(color)
    trt.begin_fill()
    trt.goto(y)
    trt.goto(z)
    trt.goto(x)
    trt.end_fill()
    trt.penup()


def square(l, x, y, color1, color2, rotation):
    cx = x + l / 2
    cy = y + l / 2

    p1 = (x, y)
    p2 = (x + l, y)
    p3 = (x + l, y + l)
    p4 = (x, y + l)

    p1 = rotate_point(p1, rotation, (cx, cy))
    p2 = rotate_point(p2, rotation, (cx, cy))
    p3 = rotate_point(p3, rotation, (cx, cy))
    p4 = rotate_point(p4, rotation, (cx, cy))

    triangle(p1, p2, p4, color1)
    triangle(p3, p4, p2, color2)


square(25, 0, 0, 'green', 'blue', 90)
square(25, 0, 25, 'green', 'blue', 90)
square(25, 0, 50, 'green', 'blue', 90)
square(25, 25, 0, 'green', 'blue', 90)
square(25, 25, 25, 'green', 'blue', 90)
square(25, 25, 50, 'green', 'blue', 90)
square(25, 50, 0, 'green', 'blue', 90)
square(25, 50, 50, 'green', 'blue', 90)
square(25, 50, 25, 'green', 'blue', 90)

square(25, -25, 0, 'green', 'blue', 0)
square(25, -25, 25, 'green', 'blue', 0)
square(25, -25, 50, 'green', 'blue', 0)
square(25, -50, 0, 'green', 'blue', 0)
square(25, -50, 25, 'green', 'blue', 0)
square(25, -50, 50, 'green', 'blue', 0)
square(25, -75, 0, 'green', 'blue', 0)
square(25, -75, 25, 'green', 'blue', 0)
square(25, -75, 50, 'green', 'blue', 0)

square(25, 0, -25, 'green', 'blue', 180)
square(25, 0, -50, 'green', 'blue', 180)
square(25, 0, -75, 'green', 'blue', 180)
square(25, 25, -25, 'green', 'blue', 180)
square(25, 25, -50, 'green', 'blue', 180)
square(25, 25, -75, 'green', 'blue', 180)
square(25, 50, -25, 'green', 'blue', 180)
square(25, 50, -50, 'green', 'blue', 180)
square(25, 50, -75, 'green', 'blue', 180)

square(25, -25, -25, 'green', 'blue', 270)
square(25, -25, -50, 'green', 'blue', 270)
square(25, -25, -75, 'green', 'blue', 270)
square(25, -50, -25, 'green', 'blue', 270)
square(25, -50, -50, 'green', 'blue', 270)
square(25, -50, -75, 'green', 'blue', 270)
square(25, -75, -25, 'green', 'blue', 270)
square(25, -75, -50, 'green', 'blue', 270)
square(25, -75, -75, 'green', 'blue', 270)


trt.done()
