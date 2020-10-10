# 4.1
myList = [5,1,8,92,7,30]
end = []

for num in myList:
    if num % 2 == 0:
        end.append(num)
print("All even numbers entered in the list: ", end)

# 4.2
a = input("Enter a list of numbers, seperated by ',': ")
aList = a.split(", ")
print(aList)