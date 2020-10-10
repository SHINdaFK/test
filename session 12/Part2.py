# 2.1
listLaptop = {
    "HP": 20,
    "DELL": 50,
    "Macbook": 12,
    "ASUS": 30
}

listLaptop["TOSHIBA"] = 10 
print(listLaptop)
# # 2.2 
new_laptop = input("What is the brand: ")
new_laptop_value = int(input("What is the laptop amounts: "))

listLaptop[new_laptop] = new_laptop_value
print(listLaptop)
# # 2.3
listLaptop['DELL'] = 60
listLaptop['Macbook'] = 2
print(listLaptop)