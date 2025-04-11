import random

secret_number = random.randint(1, 10)
attempts = 0

while (guess := int(input("Guess the number (1-10): "))) != secret_number:
    print("Too low!" if guess < secret_number else "Too high!")
    attempts += 1

print(f"🎉 Correct! You guessed it in {attempts + 1} attempts.")
