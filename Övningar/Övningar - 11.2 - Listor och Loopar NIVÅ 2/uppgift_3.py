# Uppgift 3: Sortera utan inbyggda funktioner (Bubble Sort)
li = []

while True:
    var = input("Skriv ett ord: ")

    # Kontrollera om användaren vill avsluta
    if var == 0:
        break
    li.append(var)

for i in range(len(li)):
    for j in range