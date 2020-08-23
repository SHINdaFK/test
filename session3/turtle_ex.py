from turtle import *

user = input("Enter times: ")

shape('turtle')

speed(-1)

for i in range(100):
    circle(100)
    left(i+2)

mainloop()