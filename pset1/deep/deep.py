def main():
    user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    great_question(user_input)

def great_question(answer):
    match answer.lower().strip():
        case "forty-two" | "forty two" | "42":
            print("Yes")
        case _:
            print("No")


main()