import time

""" 
print("\nÖvningar - 08 » While-loopar")
print("=============================\n")

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

time.sleep(1) """

print("\n3. Loop för användarinput (while och break)")
ans = None
while True:
    ans = input("Skriv ett tal: ")
    if ans == "0": break
#end while