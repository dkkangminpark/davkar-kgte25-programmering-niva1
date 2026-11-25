# Uppgift 6
text = "python är roligt och python är populärt"
myDic = {}
textArray = text.lower().split()
for i in textArray:
    if i not in myDic:
        myDic.update({i: textArray.count(i)})
print(myDic)
