myClass = ["Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh", "Hiep", "Long", "Nam Khanh"] 

for i in range(len):
    print("Hello ", myClass(i))


status = True
while status:
    for i in range(2):
        for y in range(4):
            x = int(input("Enter your first number: "))
            y = int(input("Enter your second number: "))
            result = x*y
            print(result)
    status = False

while True:
    user = int(input("Enter your number: "))
    print(user%3)
    break

# For xy range
count = 0
for i in range(4):
    count += i
    print("Lan chay thu ", i+1)
    print(count)

# Range (start, end, step)
for i in range (0, 100, 2):
    print(i)

for i in range(100, -2, -2):
    print(i, end = " ")

for i in range(0, 102, -2):
    print(i, end = " ")



