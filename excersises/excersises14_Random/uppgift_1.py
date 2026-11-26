# Uppgift 1
import random

var = random.randint(1, 100)
guess = None

while guess != var:
    user_input = input("Guess the number: ")
    try:
        guess = int(user_input)
        if guess == var:
            print("Congrats you FUCKER")
        elif guess > var:
            print("Too FKN high")
        else:
            print("Too FKN low")
    except ValueError:
        print("Please enter a valid number.")
