def main():
    user_input = input("Input phrase: ")
    smiley(user_input)


def smiley(phrase):
    new_phrase = phrase.replace(":)", "🙂").replace(":(","🙁")
    print(new_phrase)


main()