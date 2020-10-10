print("list into") #create
list_mon_an = ['Thit cho', 'thit meo']
mon_an_moi = input()
list_mon_an.append(mon_an_moi)
list_mon_an.append('thit ga')
mon_thit_cho = list_mon_an[0]
length = len(list_mon_an)
for i in range(length):
    print(list_mon_an[i])
print(list_mon_an)

for item in list_mon_an: #read
    print(item)
    # print(list_mon_an)
for index, item in enumerate(list_mon_an):
    print(index, item)

list_mon_an[0] = 'cho thit' #update
list_mon_an.remove('cho thit') #delete by value
list_mon_an.pop(1) #delete by index
print(list_mon_an)