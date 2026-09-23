import time

print("\nÖvningar - 11 » Listor och Loopar")
print("=============================\n")

print("\nNivå 1 - Kom igång")
print("============\n")

print("1. Samla ord i en lista")
li = []
while True:
    var = input("Skriv något (STOP för att avsluta): ")
    if var == "STOP": break
    else: li.append(var)
print(li)