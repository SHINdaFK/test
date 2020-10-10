# # 3.1
colorList = ["red", "green", "blue"]

print("Our list:\n\n", colorList)

addtolist = input("\nEnter a new color: ")

colorList.append(addtolist)

print("\nOur new list: \n\n", colorList)
numList = [5, 1, 8, 92, -1, 30]

guess = int(input("Enter a number: "))

if guess in numList: 
    print("Found, position", numList.index(guess)+1)
else:
    print("Not found in our list.")


print(sum(numList))

# 3.2
numList = [5, 1, 8, 92, -1, 30]
print("Sum of all numbers: ", sum(numList))

result = 0
for i in numList:
    result += i
print(result)

# 3.3 
x = input("Enter a list of numbers, seperated by ' ': ")
Listnum = x.split(' ')
total = 0
for i in Listnum:
    total += int(i)
print("Sum of all entered numbers: ", total)