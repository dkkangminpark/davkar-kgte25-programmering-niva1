# Uppgift 10
pos = []
neg = []
var = None
while True:
    var = int(input("Skriv in ett heltal (0 avslutar): "))
    if var == 0:
        break
    if var % 2 == 0:
        pos.append(var)
    elif var % 2 == 1:
        neg.append(var)
    else: 
        break
# end while
print(pos)
print(neg)