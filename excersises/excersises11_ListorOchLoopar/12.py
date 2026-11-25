# Uppgift 12
array = []

while True:
    ordet = input("Skriv in ett ord (eller 'stopp' för att avsluta): ")
    if ordet.lower() == "stopp":
        break
    array.append(ordet)

if array:
    langsta = max(array, key=len)
    kortaste = min(array, key=len)
    print("Det längsta ordet är:", langsta)
    print("Det kortaste ordet är:", kortaste)
else:
    print("Du skrev inga ord.")