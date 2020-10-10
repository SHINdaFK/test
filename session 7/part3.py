# # 3.1
# numList = [5, 1, 8, 92, -1, 30]

# a = input("Enter a number: ")

# for index in enumerate(numList):
#     if a == numList:
#         print("Found", index)
#     else:
#         print("Not found")

# 3.2
numList = [5, 1, 8, 92, -1, 30]
print("Sum of all numbers: ", sum(numList))


# 3.3 
x = input("Enter a list of numbers, seperated by ' ': ")
Listnum = x.split(' ')
total = 0
for i in Listnum:
    total += int(i)
print("Sum of all entered numbers: ", total)    