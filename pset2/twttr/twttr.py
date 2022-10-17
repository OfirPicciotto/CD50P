def main():
    user_input = input("Enter a phrase: ")
    vowel_remover(user_input)


def vowel_remover(phrase):
    vowels = ["a", "e", "i", "o", "u"]
    new_phrase = ""
    for letter in phrase:
        if letter.lower() in vowels:
            continue
        else:
            new_phrase += letter
    print(new_phrase)

main()