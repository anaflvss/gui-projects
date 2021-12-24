import numpy as np


def guess_number(random_int):
    print("Enter an integer from 0 to 100:")

    x = input()

    if int(x) < random_int:
        print("Too low! Try again.")
        guess_number(random_int)

    elif int(x) > random_int:
        print("Too high! Try again.")
        guess_number(random_int)

    else:
        print("That's correct! How did you know?")


# set a random number to be guessed.
random_int = np.random.randint(100)
# print(random_int)

print("\nWelcome to 'GUESS THE NUMBER'! Try to guess what number I'm thinking of. :)")
guess_number(random_int)
