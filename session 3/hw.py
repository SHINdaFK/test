for i in range(0, 7, 1):
    print(i, end = " ")

for i in range(100, 106, 1):
    print(i, end = " ")

for i in range(9, 1, -1):
    print(i, end = " ")

for i in range(0, 21, 1):
    print(i)

n = int(input("Enter a number: "))
for i in range(0, n, 1):
    print(i)

for i in range(5, 13, 1):
    print(i)

for i in range(5, n, 1):
    n = int(input("Enter a number: "))
    print(i)

for i in reversed(range(20, 9, -1)):
    print(i)

n = int(input("Enter your number: "))
m = int(input("Enter your number: "))

for i in reversed(range(n, m)):
    if condition: n > m,
        else print(i)
        else print("error message")

from turtle import *
shape('turtle')
fillcolor("yellow")
begin_fill()
for i in range(3):
    forward(100)
    left(120)

end_fill()

mainloop()

from turtle import *
shape('turtle')
fillcolor("yellow")
begin_fill()
for i in range(1):
    circle(100)

end_fill()

mainloop()

from turtle import *
shape('turtle')
fillcolor("yellow")
begin_fill()
for i in range(6):
    circle(100)
    left(60)

end_fill()

mainloop()

    
N = int(input("Count: "))

allsum = 0
b = 0

while b<= N:
    allsum = allsum + b
    b += 1

print(allsum)