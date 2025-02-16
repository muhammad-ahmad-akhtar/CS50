import random
import sys

try:
    level = int(input("Level: "))
except ValueError:
    pass
else:
    random_number = random.randint(1, int(level))

    while True:
        try:
            user_guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if user_guess == random_number:
                print("Just Right!")
                break
            elif int(user_guess) < random_number:
                print("Too small!")
            elif int(user_guess) > random_number:
                print("Too large!")
sys.exit(1)