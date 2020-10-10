from turtle import *
shape('turtle')
fillcolor("yellow")
begin_fill()
for i in range(3):
    forward(100)
    left(120)

end_fill()

mainloop()

n = int(input("Enter your number: "))

for i in reversed(range(0, n)):
    print(i)




