import time
import random

print("\nÖvningar - 10 » Listor")
print("=============================\n")

""" print("\nNivå 1 - Grundläggande listor")
print("============\n")

print("1. Skapa en lista med tre frukter och skriv ut den.")
fruit_list = ["Banana", "Apple", "Pineapple"]

for fruits in fruit_list:
    print(fruits)
# end for

time.sleep(1)

print("\n2. Skapa en tom lista och lägg till tre namn med append(). Skriv ut listan.")
na_li = []
na_li.append("P Diddy")
na_li.append("Jeffrey Epstein")
na_li.append("Donald J. Trump")
for names in na_li:
    print(names)
# end for

time.sleep(1)

print("\n3. Skapa en lista med fem tal. Skriv ut de första och sista talet med index.")
three_li = [21, 54, 65, 98, 42]
print(three_li[0], three_li[-1])

time.sleep(1)

print("\n4. Skapa en lista med fem färger")
colors_list = ["Rosa", "Blå", "Röd", "Grön", "Brun"]
colors_list[2] = "Lila"
print(colors_list)

time.sleep(1)

print("\nNivå 2 - Indexering och Slicing")
print("============\n")

print("1. Skapa en lista med sju bokstäver. Skriv ut bokstävenra från index 2-5 med slicing")
char_list = ["a", "b", "c", "d", "e", "f", "g"]
print(char_list[2:6])

time.sleep(1)

print("\n2. Skapa en lista med fem djur. Skriv ut det näst sista djuret med negativ indexering.")
animal_list = ["Hund", "Katt", "Häst", "Kanin", "Lejon"]
print(animal_list[-2])

time.sleep(1)

print("\n3. Skapa en lista med fem städer. Skriv ut de tre första med slicing")
city_list = ["Stockholm", "Göteborg", "Malmö", "Halmstad", "Värö"]
print(city_list[1:4])

print("\n4. Skapa en lista med fem siffror. Skriv ut de alla utom den sista med slicing.")
city_list = ["Stockholm", "Göteborg", "Malmö", "Halmstad", "Värö"]
print(city_list[1:4])

time.sleep(1)

print("\nNivå 3 - Iteration & längd")
print("============\n")

print("1.Skapa en lista med fem maträtter. Skriv ut varje maträtt med en for-loop.")
food_list = ["Pizza", "Tacos", "Sushi", "Köttbullar", "Lasagne"]
for food in food_list:
    print(food)
#end for

time.sleep(1)

print("\n2. Skapa en lista med sju tal. Skriv ut hur många tal som finns med len().")
tal = [1, 4, 3, 2, 6, 5, 9]
print(len(tal))

time.sleep(1)

print("\n3. Skapa en lista med fem namn. Skriv ut varje namn tillsammans med dess index")
names = ["Anes", "Anes 2", "Anes 3", "Anes 4"]
print(f"{names[0]} - {names.index(names[0])}\n{names[1]} - {names.index(names[1])}\n{names[2]} - {names.index(names[2])}\n{names[3]} - {names.index(names[3])}")

time.sleep(1)
 """
print("\nNivå 4 - Modifiering och borttagning")
print("============\n")

print("1. Skapa en lista med fyra färger. Ta bort en färg med remove() och skriv ut listan.")
colors = ["Maroon", "Turquoise", "Crimson", "Blue"]
colors.remove("Maroon")
print(colors)

time.sleep(1)

print("\n2. Skapa en lista med fem siffror. Ta bort talet på index 2 med del och skriv ut listan")
numbers = [1, 4, 7, 9, 3]
del numbers[2]
print(numbers)

time.sleep(1)

print("\n3. Skapa två listor med fem siffor. Lägg ihop dem med extend() och skriv ut den nya listan")
list_one = [1, 2, 3, 4, 5]
list_two = [6, 7, 8, 9, 10]
list_one.extend(list_two)
print(list_one)

print("\nNivå 5 - Kombinera flera moment")
print("============\n")

print("1. Skapa en lista med fem slumpmässiga tal. Sortera listan med sort() och skriv ut den. Skriv sedan ut det största och minsta talet med index.")
li = []
for i in range(5):
    li.append(random.randint(1, 101))
print(li)
print(f"1:a -> {li[0]}. 2:a -> {li[-1]}")