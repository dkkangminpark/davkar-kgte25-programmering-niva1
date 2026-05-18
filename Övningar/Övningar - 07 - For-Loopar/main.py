import time

print("\nÖvningar - 07 » For-loopar")
print("=========================\n")

""" print("1. Räkna från 1 till 10")
for n in range(1,11): print(n)
#end for

time.sleep(1)

print("\n2. Räkna baklänges")
for n in range(10): print(10-n)

time.sleep(1)

print("\n3. Upprepa text")
word = input("Skriv in ett ord: ")
for x in range(5): print(word)

time.sleep(1)

print("\n4. Multiplikationstabell för 7")
for x in range(1,11): print(x*7)

time.sleep(1)

print("\n5. Summan av talen 1-100")
sumOfNumbers = 0
for x in range (1,101): sumOfNumbers += x
print(sumOfNumbers)

time.sleep(1)

print("\n6. Upp till n")
ans = int(input("Skriv ett tal: "))
for x in range(1, ans+1): print(x)

time.sleep(1)

print("\n7. Skriva ut bokstäver med .join()")
mening = input("Skriv en mening: ")
print("*".join(mening))

time.sleep(1)

print("\n7. Skriva ut bokstäver med for-loop")
mening = input("Skriv en mening: ")
resultat = ""

for tecken in mening:
    resultat += tecken + "*"

# Ta bort sista *
resultat = resultat[:-1]

print(resultat)

time.sleep(1)

print("\n8. Triangel av stjärnor")
for x in range(1,6):
    print('*' * x) """
#end for

print("\n9. Multiplikationstabell i tabellform (dubbla for-loopar)")
for x in range(1,11):
    for y in range (1,11):
        print(str(x) + " x " + str(y) + " = " + str(x*y))