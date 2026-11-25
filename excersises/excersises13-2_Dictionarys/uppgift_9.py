# Uppgift 9
data = [
    ("Anna", "Stockholm"),
    ("Olle", "Göteborg"),
    ("Lisa", "Stockholm"),
    ("Per", "Malmö"),
]
myDic = {}
for i in data:
    stad = i[1]
    namn = i[0]
    
    if stad in myDic:
        myDic[stad].append(namn)
    else:
        myDic[stad] = [namn]
print(myDic)
