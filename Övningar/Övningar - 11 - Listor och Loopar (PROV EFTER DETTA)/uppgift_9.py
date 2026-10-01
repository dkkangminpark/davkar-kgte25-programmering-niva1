#Uppgift 9
li = []
var = None
while True:
    var = input("Skriv in ord (STOP avslutar): ")
    if var == "STOP":
        break
    li.append(var)
#end while

unika_ord = []
for x in li:
    if li.count(x) == 1:
        unika_ord.append(x)

print(unika_ord)
