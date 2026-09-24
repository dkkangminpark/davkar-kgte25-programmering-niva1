import time

print("\nÖvningar - 11 » Listor och Loopar")
print("=============================\n")

print("\nNivå 1 - Kom igång")
print("============\n")

""" print("1. Samla ord i en lista")
li = []
while True:
    var = input("Skriv något (STOP för att avsluta): ")
    if var == "STOP": break
    else: li.append(var)
print(li)

time.sleep(1)

print("\n3. Summera inmatade tal")
li = []
while True:
    var = int(input("Skriv in ett heltal (0 avslutar): "))
    if var == 0: break
    else: li.append(var)
print(li)

time.sleep(1) """

print("\n4. Räkna hur många tal som är positiva/negativa")
li = []
neg = 0
pos = 0
""" neg = []
pos = [] """
while True:
    var = int(input("Skriv in ett heltal (0 avslutar): "))
    if var == 0: break
    else: li.append(var)

for tal in li:
    if tal < 0:
        neg +=1
print(f"POS: {len(li)-neg}")
print(f"NEG: {neg}")

""" for x in range(len(li)):
    if li[x] > 0: pos.append(li[x])
    else: neg.append(li[x])
    x += 1
print(f"POS: {len(pos)}")
print(f"NEG: {len(neg)}") """

""" for tal in li:
    if tal < 0:
        neg +=1
    else:
        pos +=1
print(f"POS: {pos}")
print(f"NEG: {neg}") """

time.sleep(1)

print("\nNivå 2 - Beräkningar efter inmatning")
print("============\n")

print("\n5. Beräkna medelvärdet")