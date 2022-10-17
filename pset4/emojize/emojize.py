from emoji import emojize

def main():
    user_emoji()


def user_emoji():
    emoji_str = input("Input an Emoji: ")
    print(emojize(emoji_str))


main()