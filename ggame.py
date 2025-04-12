import random


number = random.randint(1, 100)

while True:
    try:
        message = int(input("Guess a number between 1 and 100: "))

        if message < number:
            print("Too low!")
        elif message > number:
            print("Too high!")
        else:
            print("Congratulations you guessed right")
            break
    except ValueError:
        print("Enter a valid number")