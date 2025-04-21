# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 99)

    print("Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 99.")

    attempts = 0

    while True:
        # Ask the user to guess the number
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


guess_the_number()
