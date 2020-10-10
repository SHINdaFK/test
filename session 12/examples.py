listDistrict = [
    {
        "name": "DD",
        "square": 117.43,
        "people": 150300
    },
    {
        "name": "BD", 
        "square": 9.224,
        "people": 247100
    },
    {
        "name": "BTL",
        "square": 43.35,
        "people": 333300
    }
]

listPeople = []
result = 0
for i in listPeople:
    listPeople.append(i['people'])
    result = max(listPeople)

districtHasMax = {}

for item in listDistrict:
    if (item['people']) == result:
        districtHasMax = item

print(districtHasMax)