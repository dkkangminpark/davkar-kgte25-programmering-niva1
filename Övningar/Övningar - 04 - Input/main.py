print("\nÖvningar - 02 » Variabler och Literaler")
print("=========================\n")

print("Nivå 1 - Enkla inputs")
print("===========\n")

print("1. Skriv ditt namn")
name = input("Vad heter du? ")
print(f"Hej {name}!")

print("\n2. Favoritmat")
favouriteFood = input("Vad är din favoritmat? ")
print(f"Vad roligt! jag tycker också om {favouriteFood}!")

print("\n3. Din stad")
yourCity = input("Vilken stad bor du i?")
print(f"Du bor i {yourCity}.")

print("\n4. ditt husdjur")
pet = input("Vilket husdjur har du? ")
print(f"Du har ett {pet}.")

print("\n5. Din favoritfilm")
favouriteFilm = input("Vilken är din favoritfilm? ")
print(f"Jag gillar också {favouriteFilm}!")



print("Nivå 2 - Tal och beräkningar")
print("===========\n")

print("\n1. Din ålder om 5 år")
age = int(input("Hur gammal är du? "))
age = age + 5
print(f"Om 5 år är du {age} år gammal")

print("\n2. Beräkna kvadrat")
ans = int(input("Skriv ett tal: "))
ans = ans**2
print(ans)

print("\n3. Dubbla ett tal")
ans = int(input("Skriv ett tal: "))
ans = 2 * ans
print(ans)

print("\n4. Omkrets av kvadrat")
ans = int(input("Hur lång är sidan på kvadraten?"))
ans = 4 * ans
print(ans)

print("\n5. Area av rektangel")
length = int(input("Skriv längden: "))
width = int(input("Skriv bredden: "))
area = length * width
print(area)

print("\nSlut på övningarna.")
