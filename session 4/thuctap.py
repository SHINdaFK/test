a = int(input("How long is your side 1: "))
b = int(input("How long is your bottom: "))
c = int(input("How long is your side 2: "))

hP = (a + b + c)/2
s = (hP * (hP -a) * (hP - b) * (hP - c)) **0.5
print(hP)
print(s)


if (a == c):
    print("Isosceles triangle")
elif (b**2 == a**2 + c**2):
    print("Right-angle triangle")
else:
    print("Normal Triangle")

