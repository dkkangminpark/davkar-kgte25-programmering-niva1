import time

print("\nÖvningar - 10 » Listor")
print("=============================\n")

print("\nNivå 1 - Grundläggande listor")
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

print("\n2. Skapa en lista med sju tal. Skriv ut hur många tal som finns med len().")
