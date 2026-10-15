import random

secret_number = random.ranndint(1,10)

while True:
    guess = int(input("Guess a number: "))

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else: 
        print("just right!")
        break