# Uppgift 11
langder = []
langre_an_medelvarde = []

while True:
	langd = int(input("Ange en elevs längd i cm (0 för att avsluta): "))
	if langd == 0:
		break
	langder.append(langd)
 
medelvarde = sum(langder) / len(langder)
for x in langder:
    if x > medelvarde:
        langre_an_medelvarde.append(x)
langder.sort()

print(f"Medelvärde: {medelvarde}\nDen längsta: {langder[-1]} och den kortaste: {langder[0]}\nLängre än medelvärdet: {langre_an_medelvarde}")
