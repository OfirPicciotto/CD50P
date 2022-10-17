from random import randint
import sys

def main():
    guess_game()


def guess_game():
    user_guess = 0
    while True:
        try:
            user_num = int(input("Level: "))
            if user_num < 1:
                continue
        except ValueError:
            continue
        else:
            number_to_guess = randint(1,user_num)
            print(number_to_guess)
            while user_guess != number_to_guess:
                try:
                    guess = int(input("Guess: "))
                    if guess > number_to_guess:
                        print("Too large!")
                    elif guess < number_to_guess:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                except ValueError:
                    pass
        sys.exit()


main()

