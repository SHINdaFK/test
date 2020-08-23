# 2.1
for i in range(3,13):
    print(i)

# 2.2
n = int(input("Enter your number: "))
for i in range(0, n):
    if n > 0:
        print(i)
    else:
        print("Enter number > 0")    

# 2.3
x = int(input("Enter your number: "))
for i in reversed(range(0, x+1)):
    if i % 2 != 0:
        print(i)

# 2.4
import turtle
t = turtle.Turtle()

n = int(input("Enter the number of the sides of the polygon: "))
l = int(input("Enter the length of the sides of the polygon: "))

for i in range(n):
    t.forward(l)
    t.right(360 / n)
mainloop()

