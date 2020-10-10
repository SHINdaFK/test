def totalFunc(allNumb):
    listNumber = []

    for i in allNumb:
        if type(i) is int:
            listNumber.append(i)

    return sum(listNumber)

while True:
    if checkTypeOfInput(sortList):
        print(totalFunc(sortList))
        break
    else:
        print("Type of input is not list. Please try again!")