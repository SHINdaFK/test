# def Larger(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)

# def evens(number):
#     if number % == 0:
#         print("This is a even number")
#     else:
#         print("This is an odd number")

# number = int(input("Enter your number: "))

# def leapYear(year):
#     if year % 4 == 0:
#         print("This is leap year")
#     else:
#         print("This is not leap year")
# year = int(input("Enter your year: "))

# sortList = [12, 'nam', 56, 'teacher', True, 2020]

# def checkTypeOfInput(input):
#     if type(input) is list:
#         return True
#     else:
#         return False


# def totalFunc(allNumb):
#     listNumber = []

#     for i in allNumb:
#         if type(i) is int:
#             listNumber.append(i)

#     return sum(listNumber)

# while True:
#     if checkTypeOfInput(sortList):
#         print(totalFunc(sortList))
#         break
#     else:
#         print("Type of input is not list. Please try again!")

# print(totalFunc(sortList))


# def sortAlphabetically(sortList):
#     sortList = input("Enter a list of numbers, seperated by ',': ")
#     aList = sortList.split('', ')
#     bList = sorted(aList)
#     print(bList)


[] # List, Array
{} # Dictionary, Object
# Question 4
# listNumber = [12, 46, True, "C4T", 100]

# result = 0
# for numb in listNumber:
#     if type(numb) is int:
#         result += numb
# print(result)

def convertStringToList(text):
    result = text.split(', ')
    result.sort()
    

userInput = input("Enter everything, seperated by ',': ")

lastResult = convertStringToList(userInput)
print(lastResult)
