print("\nÖvningar - 02 » Variabler och Literaler")
print("=========================\n")

print("1. Enkla variabler och utskrifter")
name = "David"
age = 16
print("Hej jag heter", name, "och är", age, "år gammal.")

print("\n2. Ändra variabelvärde")
city = "Götlaborg"
print(city)
city = "Halmstad"
print(city)

print("\n3. Flervärdes-tilldelning")
a, b, c = 5, 3.2, "Hej"
print(a)
print(b)
print(c)

print("\n4. Samma värde till flera variabler")
x = y = "Python"
print(x)
print(y)

print("\n5. Variabelnamn — regler och praktik")
print('"snake_case" är giltig eftersom den börjar med liten bokstav och innehåller en "_"')
print('"2nd_place" är INTE giltig eftersom den börjar med en siffra')
print('"camelCase" är giltig eftersom den börjar med liten bokstav och i pratiken ska man ha stor bokstav vid början utav ord efter det första')
print('"class" är INTE giltig eftersom det är ett reserverat ord i Python')
print("\nMina tre egna variabler är:")
print("1. pyVar")
print("2. my_variable")
print("3. davidsFantastiska_variabel")

print('\n6. Begreppet "konstanter" i programmering')
PI = 3.14159 # Konstant för pi
""" 
I python finns inga riktiga konstanter, men en oskriven regel är att variabler som skrivs med stora bokstäver inte ska ändras.
Därav går det ändå att ändra
"""
print("Värdet av konstanten PI är:", PI)
PI = 3 # Därför går det nu att ändra värdet av "PI"
print("Efter att ha ändrat värdet av PI är det nu:", PI)

print("\n7. Sammansätt sträng med f-string")
name = "David"
age = 16
print(f"Jag heter {name} och är {age} år gammal.")

print("\n8. Kodgranskning — identifiera literaler och variabler")
a = 1
b = 2
c = a + b
print(c)
print("Det finns 3 variabler eftersom de kan variera (a,b,c). Däremot finns endast 2 literaler (1 och 2 eftersom de inte förändras.). Därav blir c=3")

print("\nSlut på övningarna.")
