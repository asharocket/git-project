import random

secret_number = random.randint(1,10)

while True:
    guess = int(input("Guess a number: "))

    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    else: 
        print("just right!")
        break