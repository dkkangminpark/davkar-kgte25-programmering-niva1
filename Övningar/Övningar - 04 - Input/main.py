import time

print("\nÖvningar - 02 » Variabler och Literaler")
print("=========================\n")

print("Nivå 1 - Enkla inputs")
print("===========\n")

print("1. Skriv ditt namn")
name = input("Vad heter du? ")
print(f"Hej {name}!")

time.sleep(1)

print("\n2. Favoritmat")
favouriteFood = input("Vad är din favoritmat? ")
print(f"Vad roligt! jag tycker också om {favouriteFood}!")

time.sleep(1)

print("\n3. Din stad")
yourCity = input("Vilken stad bor du i? ")
print(f"Du bor i {yourCity}.")

time.sleep(1)

print("\n4. ditt husdjur")
pet = input("Vilket husdjur har du? ")
print(f"Du har ett {pet}.")

time.sleep(1)

print("\n5. Din favoritfilm")
favouriteFilm = input("Vilken är din favoritfilm? ")
print(f"Jag gillar också {favouriteFilm}!")

time.sleep(1)

print("Nivå 2 - Tal och beräkningar")
print("===========\n")

print("\n1. Din ålder om 5 år")
age = int(input("Hur gammal är du? "))
age = age + 5
print(f"Om 5 år är du {age} år gammal")

time.sleep(1)

print("\n2. Beräkna kvadrat")
ans = int(input("Skriv ett tal: "))
ans = ans**2
print(ans)

time.sleep(1)

print("\n3. Dubbla ett tal")
ans = int(input("Skriv ett tal: "))
ans = 2 * ans
print(ans)

time.sleep(1)

print("\n4. Omkrets av kvadrat")
ans = int(input("Hur lång är sidan på kvadraten? "))
ans = 4 * ans
print(ans)

time.sleep(1)

print("\n5. Area av rektangel")
length = int(input("Skriv längden: "))
width = int(input("Skriv bredden: "))
area = length * width
print(area)

time.sleep(1)

print("Nivå 3 - Flera Inputs")
print("===========\n")

print("\n1. Fullständigt namn")
forNamn = input("Vad heter du i förnamn? ")
efterNamn = input("Efternamn? ")
print(f"Hej {forNamn} {efterNamn}")

time.sleep(1)

print("\n2. Favoritbok och författare")
favoritBok = input("Vad är din favoritbok? ")
author = input("Vem har skrivit den? ")
print(f"Du gillar '{favoritBok}' av {author}")

time.sleep(1)

print("\n3. Tre favoritämnen")
print("Vad är dina tre favoritämnen?")
subject1 = input("Skriv ditt första favoritämne: ")
subject2 = input("Skriv ditt andra favoritämne: ")
subject3 = input("Skriv ditt tredje favoritämne: ")
print(f"Dina favoritämnen är {subject1}, {subject2} och {subject3}.")

print("\n3b. Tre favoritämnen (MED SPLIT) (separatorn är ', ')")
subjects = input("Vad är dina tre favoritämnen (separera med ', '): ")
subjects = subjects.split(", ")
print(f"Dina favoritämnen är {subjects[0]}, {subjects[1]} och {subjects[2]}.")

time.sleep(1)

print("\n4. Medelvärde av två tal")
print("Skriv två tal")
firstNumber = int(input("Första talet: "))
secondNumber = int(input("Andra talet: "))
result = (firstNumber + secondNumber) / 2
print(result)

time.sleep(1)

print("\n4b. Medelvärde av två tal (MED SPLIT) (separatorn är ', ')")
numbers = input("Skriv två tal: ")
numbers = numbers.split(", ")
result = (int(numbers[0]) + int(numbers[1])) / 2
print(result)

time.sleep(1)

print("\n5. Pris med moms")
exklMoms = float(input("Vad kostar varan? "))
inklMoms = exklMoms*1.25
print(f"{inklMoms} kr")

print("\nSlut på övningarna.")
