from turtle import *

tracer(0)
screensize(5000, 5000)
r = 20
for i in range(2):
    fd(17 * r)
    lt(90)
    fd(10 * r)
    lt(90)
up()
bk(4 * r)
rt(90)
bk(3 * r)
lt(90)
down()
for i in range(2):
    fd(40 * r)
    rt(90)
    fd(10 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()