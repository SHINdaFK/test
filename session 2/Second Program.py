from turtle import *
times = int(input("enter here: "))
shape("turtle")
color("red")
speed(-1)

for x in range(times):
    for i in range (4):
        forward(100)
        left(90)
    left(10)
mainloop()

name = input("What is your name:")
print("Hello " + name + "! Welcome to Mindx")