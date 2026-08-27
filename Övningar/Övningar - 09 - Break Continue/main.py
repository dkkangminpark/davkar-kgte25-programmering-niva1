import time

""" 
print("\nÖvningar - 08 » While-loopar")
print("=============================\n")

print("\nDel 1: Enkla loopar (Svårighetsgrad 1–3)")
print("============\n")

print("1. Stoppa räkningen tidigt (break)")
for x in range(1,11):
    print(x)
    if x == 5: break
#end for

time.sleep(1)

print("\n2. Hoppa över ett tal (continue)")
for x in range(1,8):
    if x == 3: continue
    print(x)
#end for

time.sleep(1)

print("\n3. Loop för användarinput (while och break)")
ans = None
while True:
    ans = input("Skriv ett tal: ")
    if ans == "0": break
#end while

time.sleep(1)

print("\nDel 2: Komplexa villkor och kombinationer (Svårighetsgrad 4–6)")
print("============\n")

print("\n4. Filtrering med continue")
for x in range(1,16):
    if x % 2 == 0: continue
    print(x)
#end for

time.sleep(1)

print("\n5. Både break och continue i samma loop")
for x in range(10, 31):
    if x == 25: continue
    print(x)
    if x == 28: break
# end for

time.sleep(1)

print("\n6. Kontrollera räknaruppdatering i while-loop (continue)")
x = 0
while x < 20:
    x += 1
    if x % 4 == 0: continue
    print(x)
#end while

time.sleep(1)"""

print("\nDel 3: Nästlade loopar och avancerad logik (Svårighetsgrad 7–10)")
print("============\n")

print("\n7. Stoppa den inre loopen (break i nästlad loop)")
for x in range(1,4):
    print(f"Yttre loop: {x}")
    for y in range(1,6):
        print(f"Inre loop: {y}")
        if y == 3: break