#Uppgift 8
li = []
var = None
while True:
    var = input("Skriv in ord (STOP avslutar): ")
    if var == "STOP": break
    li.append(var)
#end while

sokt_ord = input("Skriv det ord du vill söka: ")
print(f"Ditt ord ('{sokt_ord}') hittades {li.count(sokt_ord)} gånger")