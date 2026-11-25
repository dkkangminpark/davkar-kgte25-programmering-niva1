# Uppgift 2: Hitta det mest frekventa ordet (Mode)
ord_lista = []

print("Mata in ord ett i taget. Skriv STOP när du är klar.")

# Steg 2: Samla in ord från användaren tills de skriver STOP
""" while True:
    text = input("Skriv ett ord: ")

    # Kontrollera om användaren vill avsluta
    if text == "STOP":
        break

    ord_lista.append(text) """

ord_lista = ["äpple", "päron", "äpple", "banan", "äpple", "päron"]
max_antal = 0

for i in range(len(ord_lista)):
    antal = ord_lista.count(ord_lista[i])

    if antal > max_antal:
        max_antal = antal
# end for

redan_visade = []

for i in range(len(ord_lista)):
    antal = ord_lista.count(ord_lista[i])

    if antal == max_antal:
        if ord_lista[i] not in redan_visade:
            print(ord_lista[i], "förekommer", antal, "gånger.")
            redan_visade.append(ord_lista[i])
