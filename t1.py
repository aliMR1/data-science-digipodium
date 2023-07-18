from turtle import *

speed('fast')
pencolor('orange')

# range(stop)
#range(start,stop)
#range(start,stop,step)

for i in range(10,30,2):
 fd(120)
 lt(360/10)
 dot(12, 'green')
 write (i, font=('Calibri',30,'bold'))

 #reverse
 goto(100,40)
 for i in range(10,0,-1):
  fd(60)
  lt(360/10)
  dot(15,'red')
  write(i,font=('Calibri',20,'bold'))

mainloop()
