import time

print("\nÖvningar - 08 » While-loopar")
print("=============================\n")

print("\nNivå 1 - Grundläggande listor")
print("============\n")

print("1. Skapa en lista med tre frukter och skriv ut den.")
fruit_list = ["Banana", "Apple", "Pineapple"]

for fruits in fruit_list:
    print(fruits)
#end for

time.sleep(1)

print("\n2. Skapa en tom lista och lägg till tre namn med append(). Skriv ut listan.")
na_li = []
na_li.append("P Diddy")
na_li.append("Jeffrey Epstein")
na_li.append("Donald J. Trump")
for names in na_li:
    print(names)