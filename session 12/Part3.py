listLaptop = {
    "HP": 20,
    "DELL": 60,
    "Macbook": 2,
    "ASUS": 30,
    "TOSHIBA": 10,
}

# 3.1
for key, value in listLaptop.items():
    print(key, ':', value)

# 3.2
sum = 0
for i in listLaptop: 
    sum = sum + listLaptop[i]
    print(sum)

# 3.3
listLaptop['FUJITSU'] = 15
listLaptop['ALIENWARE'] = 5
print(listLaptop)

# 3.4
sum = 0
for i in listLaptop: 
    sum = sum + listLaptop[i]
    print(sum)