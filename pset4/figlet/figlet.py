import sys
import random
from pyfiglet import Figlet

Figlet = Figlet()
fonts = Figlet.getFonts()

def main():
    get_string()


def get_string():

    if len(sys.argv) == 1:
        print("here")
        user_txt = input()
        rnd_font = random.choice(fonts)
        Figlet.setFont(font = rnd_font)
        print(Figlet.renderText('user_txt'))
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font_idx = fonts.index(sys.argv[2])
            try:
                user_font = fonts[font_idx]
            except IndexError:
                sys.exit("Invalid usage")
            else:
                user_txt = input()
                Figlet.setFont(font = user_font)
                print(Figlet.renderText(user_txt))
        else:
            sys.exit("Invalid usage")
    else:
            sys.exit("Invalid usage")


main()