import time

print("\nÖvningar - 06 » If-satser")
print("=========================\n")

"""print("Nivå 1 - Enkla vilkor")
print("===========\n")

print("1.")
tal = input("Skriv ett tal: ")
tal = int(tal)
if (tal > 10): print("Stort tal")

time.sleep(1)

print("\n2.")
namn = input("Skriv ett namn: ")
if (namn == "Alice"): print("Hej Alice!")

time.sleep(1)

print("\n3.")
tal = input("Skriv ett tal: ")
tal = int(tal)
if tal < 0:
    print("Negativt tal")

print("Nivå 2 - If och Else")
print("===========\n")

print("1. Fråga efter tal")
ans = input("Skriv ett tal: ")
if (int(ans) % 2 == 0): print("Jämnt tal")
else: print("Udda tal")

time.sleep(1)

print("\n2. Fråga efter ålder")
age = input("Hur gammal är du? ")
if (int(age) < 18):
    print("Du är mindreårig") 
else:
    print("Du är myndig")
#end if

time.sleep(1)


print("Nivå 3 - Flera villkor med elif")
print("===========\n")


print("1. Fråga efter ett betyg")
# Använder myDic
myDic = {"A": "Utmärkt", "B": "Bra jobbat!", "C":"Godkänt.", "D":"Behöver förbättras", "F":"Underkänt"} # Om jag vill använda myDic
ans = input("Skriv ditt betyg: ")
if ans in myDic: print(myDic[ans])
else: print("Du har inte skrivit in något betyg!")

time.sleep(1)

# Använder if-elif-else
ans = input("Skriv ditt betyg: ")
if (ans == "A"): print("Utmärkt!") 
elif (ans == "B"): print("Bra jobbat!")
elif (ans == "C"): print("Godkänt.")
elif (ans == "D"): print("Behöver förbättras.")
elif (ans == "F"): print("Underkänt.")
else: print("Du har inte skrivit in något betyg!")
# end if

time.sleep(1)

print("\n2. Fråga efter temeratur")
temp = input("Vad är temperaturen: ")
if (int(temp) > 20): print("Varmt")
elif (int(temp) < 10): print("Kallt")
elif (int(temp) <= 20 and int(temp) >= 10): print("Lagom")
else: print("Ej giltigt svar")

time.sleep(1)
"""

