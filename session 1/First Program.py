# range(n)
# start = 0, stop = n, step = 1
print(*range(5))
print(*range(0, 101, 2))

# variable name = "blah blah" (note valuable name cannot contain space or special symbols)
# name = "hiep" (correct)
# City name = "Hanoi" (wrong because there is a space between "city" and "name")

age = 16
name = "tuan anh"
print("hello " + name, age)

name = input("enter your name: ")
print("Hello " + name)

# let n = a value then do the math lmao
a = 2
b = 5
print(a*b)

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = (a + b) / 2
print(c)