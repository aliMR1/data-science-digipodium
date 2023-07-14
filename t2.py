from turtle import *

speed('fast')
pencolor('blue')
bgcolor('#303030')
pensize(1)

i=200
while i>0:
    fd(i)
    lt(90)
    i -= 4

mainloop()