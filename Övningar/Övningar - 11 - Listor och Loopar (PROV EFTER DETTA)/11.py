# Uppgift 11
längder = []
langre_an_medelvarde = []

while True:
	längd = int(input("Ange en elevs längd i cm (0 för att avsluta): "))
	if längd == 0:
		break
	längder.append(längd)
medelvarde = sum(längder) / len(längder)
for x in längder:
    if x > medelvarde:
        langre_an_medelvarde.append(x)
