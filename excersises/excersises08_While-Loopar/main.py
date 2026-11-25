import time
from random import *

print("\nÖvningar - 08 » While-loopar")
print("=============================\n")

print("1. Räkna från 1 till 10")
x = 1
while x <= 10:
    print(x)
    x += 1
#end while

time.sleep(1)

print("\n2. Summera talen 1-100")
n = 1
total = 0
while n <= 100:
    total += n
    n += 1
print(f"Summan av talen 1-100 är: {total}")

time.sleep(1)

print("\n3. Gissa talet (enkel version)")
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Gissa det hemliga talet: "))
    print("Fel! Försök igen.")
#end while
print("Grattis! Du gissade rätt!")

time.sleep(1)

print("\n4. Räkna ner")
count = int(input("Ange ett startnummer: "))
while count >= 0:
    print(count)
    count -= 1
#end while

time.sleep(1)

print("\n5. Multiplikationstabell")
number = int(input("Ange ett tal för att se dess multiplikationstabell: "))
n = 1
while n <= 10:
    print(f"{number} x {n} = {number * n}")
    n += 1
#end while

time.sleep(1)

print("\n6. Summera tills användaren skriver 0")
summa = 0
ans = None
while ans != 0:
    ans = int(input("Skriv ett heltal: "))
    summa += ans
#end while
print(summa)

time.sleep(1)

print("\n7. Antal försök")
n = 0
ans = None
while ans != 12:
    ans = int(input("Gissa talet: "))
    print("Fel!")
    n += 1
#end while
print(f"Rätt, talet var 12. Och du gissade rätt på {n} försök.")

time.sleep(1)

print("\n8. Stjärnmönster en rad i taget")
n = int(input("Skriv ett tal: "))
x = 1
while x != n+1:
    print("*" * x)
    x += 1
#end while

time.sleep(1)

print("\n9. Miniräknare med meny")
val = None
while val != "3":
    val = input("1. Addera två tal\n2. Subtrahera två tal\n3. Avsluta\n")
    if val == "1":
        a = float(input("Första talet: "))
        b = float(input("Andra talet: "))
        print(f"Resultat: {a + b}")
    elif val == "2":
        a = float(input("Första talet: "))
        b = float(input("Andra talet: "))
        print(f"Resultat: {a - b}")
    elif val == "3":
        print("Avslutar.")
    else:
        print("Ogiltigt val, försök igen.")
# end while

time.sleep(1)

print("\n10. Gissa talet (avancerad)")
tal = 158
#randint(1,100)
ans = None

while ans != tal:
    ans = input("Gissa talet: ")
    if int(ans) > tal: print("För högt!")
    else: print("För lågt!")
#end while
print("Rätt!")