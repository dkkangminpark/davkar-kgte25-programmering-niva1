# Uppgift 7
myDic = {}
d = {"a": 1, "b": 2, "c": 3}
for i in d:
    myDic.update({d[i]: i})
d = myDic
print(d)