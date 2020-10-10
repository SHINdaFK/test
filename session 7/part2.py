# 2.1 
colorList = ['blue', 'red', 'teal', 'green']
a = int(input("Enter position: "))
if a in colorList:
    print(colorList)

# 2.2
colorList = ["red", "orange", "blue", "teal"]
print("Our color list:")
for i in colorList:
    print((colorList.index(i)+1),"\b.", i)

numbers = ["1", "2", "3", "4"]
userRemove = input("Item to remove:")
if userRemove in numbers:
    userRemove = int(userRemove) - 1
    colorList.pop(userRemove)
elif userRemove in colorList:
    colorList.remove(userRemove)
else:
    print("No item have been removed")

print(colorList)

# 2.3
from turtle import *
color("blue")
forward(50)
color("red")
forward(50)
color("green")
forward(50)
mainloop()