# Uppgift 6
li = []
var = None
while True:
    var = int(input("Skriv in ett heltal (0 avslutar): "))
    if var == 0: break
    li.append(var)
#end while

li.sort()
print(f"LISTAN: {li}\nMINSTA: {li[0]}\nSTÖRSTA: {li[-1]}")