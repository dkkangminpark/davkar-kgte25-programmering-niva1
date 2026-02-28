import time

print("\nÖvningar - 03 » Operatorer")
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

print("\nSlut på övningarna.")
