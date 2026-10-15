import random

# Generate a random number between 1 and 100
secret_number = random.randint(1,100)

guess = None

while guess != secret_number:
    guess = int(input("Guess a number: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You goit it!")