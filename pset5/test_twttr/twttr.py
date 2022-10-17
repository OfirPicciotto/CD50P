def main():
    user_input = input("Enter a phrase: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_phrase = ""
    for letter in word:
        if letter.lower() in vowels:
            continue
        else:
            new_phrase += letter
    return new_phrase


if __name__ == "__main__":
    main()
