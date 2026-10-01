# Uppgift 7
li = []
var = None
while True:
    var = int(input("Skriv in ett heltal (0 avslutar): "))
    if var == 0:
        break
    if var % 2 == 0:
        li.append(var)
# end while
print(li)
