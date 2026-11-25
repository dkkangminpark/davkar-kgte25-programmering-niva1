# Uppgift 8
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
myDic = {}
for i in b:
    if i not in myDic:
        myDic.update({i: b[i]})
# end for

for i in a:
    if i not in myDic:
        myDic.update({i: a[i]})
# end for

print(myDic)