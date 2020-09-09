myNumbers = [1,3,7,9,10,23]
print(sum(myNumbers))
result = 0 

userInput = input("Enter list items and split by (,): ")

favourite = ['esport', 'soccer', 'pes', 'motor']
print(favourite)

for i in favourite:
    if i == 'soccer':
        print(i)
    else:
        break

if 'soccer' in favourite:
    print("Hello")
else:
    print("Not found") 

favourite[0] = 'sport'
print(favourite)

favourite.append('badminton')
print(favourite)

favourite.pop()