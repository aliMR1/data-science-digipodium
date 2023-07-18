from turtle import *

speed('fastest')
colors=['red','blue','green','brown']
pensize(3)
for i in range(100):
   # print(i%4, colors[i%4])
   pencolor(colors[i%4])
   fd(i*2)
   lt(180)
   circle(i*2, 30)

mainloop()