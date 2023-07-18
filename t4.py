from turtle import *
speed('fastest')
pensize(3)
bgcolor('black')
pencolor('white')
side = 6
for i in range(side):
    fd(200)
    for i in range(side):
        fd(100)
        lt(360/side)
        for i in range (side):
            fd(50)
            lt(360/side)
    lt(360/side)
    
mainloop()