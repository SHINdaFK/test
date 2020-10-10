# 3.1
x = int(input("Enter your number: "))
if x > 13:
    print(x)
else:
    print("x is smaller than 13")

# 3.2
x = int(input("Enter your number: "))
if (x % 2) == 0 :
    print("{0} is even number".format(x))
else:
    print("{0} is odd number".format(x))

# 3.3
month = input("Enter your month: ")

if month == 'September' or month == 'April' or month == 'June' or month == 'November':
    print(30)
elif month == 'January' or month == 'March' or month == 'May' or month== 'July' or month == 'August' or month == 'October' or month== 'December':
    print(31)
elif month == 'February':
    print(28, "or", 29)

else:
    print('Blank')