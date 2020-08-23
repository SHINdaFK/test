from random import *

a = randrange(10)
b = randrange(10)
correct = a + b
wrongNumber = [-1, 0 , 1]
chosenNumber = choice(wrongNumber)

incorrect = correct + chosenNumber

print(a, "+", b, "=", incorrect)
userInput = input("True or False (T/F): ")
if correct != incorrect:
    if userInput.lower() == "t":
        print("You lost")
    elif userInput.lower() == "f":
        print("You win")
else:
    if userInput.lower() == "t":
        print("You win")
    elif userInput.lower() == "f":
        print("You lost")




#    for book in books:
#        if userInput == book.lower():
#            print(book)
#            break
#    else:
#       print("Not found")

books = [
        "Book 1", "Harry Potter", "Romeo Juliet", "Su tich cay khe", "Thach Sanh"
]

while True:
    userInput = input("Enter here: ")
    if userInput in books:
        index = books.index(userInput)
        print(books[index])
        break
    else:
        print("Not found")

# Syntax
#if condition 1:
#   statements if condition 1 is true
#elif condition 2:
#   statements if condition 2 is true
#elif condition 3:
#   statements if condition 3 is true
#else:
#   statements if none is true

age = int(input("How old are you: "))

if age <= 6:    #baby
    print("Baby")
elif 6 < age <= 13:   #kid
    print("Kid")
elif 13 < age <= 17:   #teen
    print("Teen")
else:   #adult
    print("Adult") 


# Conditional

a = 23
b = int(input("Enter your number: "))
if b >= a:
    print("b is greater than a")
else:
    print("b is less than a")




