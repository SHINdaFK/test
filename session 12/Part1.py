# 1.1
listLaptop = {
    "HP": 20,
    "DELL": 50,
    "Macbook": 12,
    "ASUS": 30
}

# 1.2
print(
    listLaptop["Macbook"]
)

# 1.3
laptop_input = input("What kind of Laptop brand do you want: ")

for i in listLaptop:
    if i == laptop_input:
        print(listLaptop[laptop_input])