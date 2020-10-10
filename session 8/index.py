# Funtion 



def reverseList():

    myList = ["Dad", "Me", "Mom"]

    print("Hello World")
    print("My Family ", myList)

    return myList

reverseList()

def printTrue():
    print("True")

if (5 < 8):
    printTrue()
elif (6 < 8):
    printTrue()

# Đặt tên đúng mục đích. Chỉ nên ghi 3 tham số
def checkAge(age):
    if (0 <= age <= 6):
        print("Baby")
    elif (7 <= age <= 15):
        print("Children")
    elif (16 <= age <= 18):
        print("Teen")
    else:
        print("adult")
    
yourAge = int(input('Enter your age: '))

checkAge(yourAge)

# vd:
def checkAge(age):
    if (0 <= age <= 6):
        return ("Baby")
    elif (7 <= age <= 15):
        return ("Children")
    elif (16 <= age <= 18):
        return ("Teen")
    else:
        return ("adult")
    
yourAge = int(input('Enter your age: '))

result = checkAge(yourAge)

print('Hello ' + result)

