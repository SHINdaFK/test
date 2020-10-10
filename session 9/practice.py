# from turtle import *
# speed(-1)

# userInput = int(input("Enter numbers of circle you want to draw: "))

# def drawTimesCircle(times):
#     for i in range(times):
#         circle(100)
#         left(i*10)

# drawTimesCircle(userInput)

# mainloop()

# Hoi nguoi dung xem la nguoi tamuon ve hinh gi? va so luong hinh ma nguoi ta muon ve

from turtle import *
speed(-1)

shapeInput = input("What shape do you want to draw: ")
Times = int(input("How many times do you want to draw: "))

def HinhHoc(Shapetype, repeatition):
    if Shapetype == "hinh vuong" or Shapetype == 'square': 
        for i in range(repeatition):
            for x in range(4):
                forward(100)
                left(90)
            left(30)
    elif shapeInput == "hinh tron" or shapeInput == 'circle':
        ban_kinh = int(input("What is your radius: "))
        for i in range(repeatition):
            circle(ban_kinh)
            left(30)

HinhHoc(shapeInput,Times)

mainloop()