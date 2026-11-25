import time

print("\nÖvningar - 05 » Operatorer")
print("=========================\n")

print("1. Addition och subtraktion")
numbers = input("Skriv två tal (separera med ', '): ")
numbers = numbers.split(", ")
addition = int(numbers[0]) + int(numbers[1])
subtraktion = int(numbers[0]) - int(numbers[1])
print(f"Addition: {addition}")
print(f"Subtraktion: {subtraktion}")

time.sleep(1)

print("\n2. Multiplikation och division")
numbers = input("Skriv två tal (separera med ', '): ")
numbers = numbers.split(", ")
multiplikation = int(numbers[0]) * int(numbers[1])
division = int(numbers[0]) / int(numbers[1])
print(f"Multiplikation: {multiplikation}")
print(f"Division: {division}")

time.sleep(1)

print("\n3. Modulus och heltalsdivision")
tal = int(input("Skriv in ett heltal: "))
modulus = tal % 5
heltalsDivision = tal // 5
print(modulus)
print(heltalsDivision)

time.sleep(1)

print("\n4. Upphöjt till (exponent)")
tal = int(input("Skriv ett tal: "))
print(tal**2)
print(tal**3)

time.sleep(1)

print("\n5. Jämförelseoperatorer")
tal = input("Skriv två tal (separera med ', '): ")
tal = tal.split(", ")
if int(tal[0]) > int(tal[1]):
    print("Det första talet är större än det andra.")
else:
    print("Det första talet är inte större än det andra")
if int(tal[0]) == int(tal[1]):
    print("Talen är lika.")
else:
    print("Talen är inte lika")
if int(tal[0]) <= int(tal[1]):
    print("Det första talet är mindre än eller lika med det andra")
else:
    print("De första talet är inte mindre eller lika med det andra talet")

time.sleep(1)

print("\n6. Logiska operatorer med True och False")
a = True
b = False
print(a and b)  # 	Returns True if both statements are true (från W3Schools)
print(a or b)  #   Returns True if one of the statements is true (från W3Schools)
print(
    not a
)  #   Reverse the result, returns False if the result is true (från W3Schools)

time.sleep(1)

print("\n7. Kombinera jämförelse och logik")
tal = input("Skriv tre tal (separera med ', '): ")
tal = tal.split(", ")
tal1 = int(tal[0])
tal2 = int(tal[1])
tal3 = int(tal[2])

if tal1 > tal2 and tal2 > tal3:
    print(
        "Det första talet är större än det andra och det andra är större än det tredje."
    )
else:
    print(
        "Det första talet är inte större än det andra och det andra är inte större än det tredje."
    )
if tal1 == tal2 or tal1 == tal3:
    print("Det första talet är lika med det andra eller tredje.")
else:
    print("Det första talet är inte lika med det andra eller tredje talet")

time.sleep(1)

print("\n8. Tilldelningsoperatorer")
var = 10
print(var)

time.sleep(0.2)
var += 3
print(var)

time.sleep(0.2)
var -= 7
print(var)

time.sleep(0.2)
var *= 3
print(var)

time.sleep(0.2)
var /= 5
print(var)

print("\nSlut på övningarna.")
