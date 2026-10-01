#Uppgift 13
temp_array = []

while True:
    temp = int(input("Mata in dagens temperatur i heltal (eller 999 för att avsluta): "))
    if temp == 999:
        break
    temp_array.append(temp)

print("Alla", sep=": ")
for x in temp_array:
    print(x, sep=", " ,end="")

print(f"\nMedelvärde: {sum(temp_array)/len(temp_array)}")

minus = 0
for x in temp_array:
    if x < 0:
        minus += 1
print(f"Antal dagar med minusgrader: {minus}")

temp_array.sort()
print(f"Högsta: {temp_array[-1]}, lägsta: {temp_array[0]}")