# Uppgift 3: Sortera utan inbyggda funktioner (Bubble Sort)
li = [1, 4, 7, 2, 9, 5]
""" 
while True:
    var = int(input("Skriv ett tal eller 0 för att avsluta"))
    if var == "0":
        break
    li.append(var) """
for grej in li:
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            temp1 = li[i]
            li[i] = li[i + 1]
            li[i + 1] = temp1
    print(li)
print(f"FÄRDIG: {li}")
