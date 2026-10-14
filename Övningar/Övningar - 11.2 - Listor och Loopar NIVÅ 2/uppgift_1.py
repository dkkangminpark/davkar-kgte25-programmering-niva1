# Uppgift 1: Hitta dubbletter och deras positioner
# Steg 1: Skapa en tom lista för att spara orden
ord_lista = []

print("Mata in ord ett i taget. Skriv STOP när du är klar.")

# Steg 2: Samla in ord från användaren tills de skriver STOP
while True:
    text = input("Skriv ett ord: ")

    # Kontrollera om användaren vill avsluta
    if text == "STOP":
        break

    ord_lista.append(text)

print("\n--- Resultat ---")

# Steg 3: Hitta dubbletter och deras positioner
kollade_ord = []

for i in range(len(ord_lista)):
    nuvarande_ord = ord_lista[i]

    # Kolla om ordet har dykt upp tidigare i listan och om vi inte redan har skrivit ut det
    if ord_lista.count(nuvarande_ord) > 1 and nuvarande_ord not in kollade_ord:
        kollade_ord.append(nuvarande_ord)

        # Hitta alla index för detta ord
        positioner = []
        for j in range(len(ord_lista)):
            if ord_lista[j] == nuvarande_ord:
                positioner.append(j)

        print(f"Ordet '{nuvarande_ord}' förekommer flera gånger på index: {positioner}")

if len(kollade_ord) == 0:
    print("Inga dubbletter hittades i listan.")
