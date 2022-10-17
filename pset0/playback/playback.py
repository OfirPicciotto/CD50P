def main():
    user_input = input("Please enter a phrase: ")
    reduce_playback(user_input)


def reduce_playback(phrase):
    print(phrase.replace(" ", "..."))


main()