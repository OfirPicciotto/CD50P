from random import randint
import sys


def main():
    num = get_level()

    errors = 1
    score = 0

    for i in range(10):
        x = generate_integer(num)
        y = generate_integer(num)
        answer = x + y
        equation = input(f"{x} + {y} = ")
        if int(equation) == answer:
             score += 1
        while int(equation) != answer:
             errors += 1
             print("EEE")
             equation = input(f"{x} + {y} = ")
             if errors == 3:
                print(answer)
                sys.exit(f"Score: {score}")
    print(f"Score: {score}")


def get_level():
    allowed_lvls = [1, 2, 3]
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl not in allowed_lvls:
                continue
            else:
                return lvl
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        range_start = 0
    else:
        range_start = 10**(level-1)
    range_end = (10**level)-1
    return randint(range_start, range_end)


if __name__ == "__main__":
    main()
