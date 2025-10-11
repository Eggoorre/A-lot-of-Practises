import turtle as trt
import math as mth

trt.penup()

trt.tracer(0)


def triangle(x, y, l, color):
    trt.fillcolor(color)
    trt.setpos(x, y)
    trt.pendown()
    trt.begin_fill()
    trt.forward(l)
    trt.right(135)
    trt.forward(l * 0.5 * mth.sqrt(2))
    trt.right(90)
    trt.forward(l * 0.5 * mth.sqrt(2))
    trt.end_fill()
    trt.penup()
    trt.home()
    pass


def rectangle(x, y, l, w, color):
    trt.fillcolor(color)
    trt.setpos(x, y)
    trt.pendown()
    trt.begin_fill()
    for i in range(2):
        trt.forward(l)
        trt.right(90)
        trt.forward(w)
        trt.right(90)
    trt.end_fill()
    trt.penup()
    trt.home()
    pass


def parallelogram(x, y, l, w, color):
    trt.fillcolor(color)
    trt.setpos(x, y)
    trt.pendown()
    trt.begin_fill()
    for i in range(2):
        trt.forward(l)
        trt.right(135)
        trt.forward(w)
        trt.right(45)
    trt.end_fill()
    trt.penup()
    trt.home()
    pass


number_of_cycles = 10
for i in range(number_of_cycles):
    parallelogram(-200 + i * 50, 0, 50, 25 * mth.sqrt(2), 'cyan')
    rectangle(-225 + i * 50, -25, 50, 50, 'purple')
    triangle(-225 + i * 50, -50, 50, 'pink')
    trt.right(180)
    triangle(-175 + i * 50, -50, 50, 'blue')
    parallelogram(-225 + i * 50, -75, 50, 25 * mth.sqrt(2), 'cyan')


trt.done()