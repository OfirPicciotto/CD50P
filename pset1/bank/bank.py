def main():
    user_input = input("Choose a greeting: ")
    greet(user_input)


def greet(greeting):
    if greeting.lower().strip().startswith("hello"):
        print("$0")
    elif greeting.lower().strip().startswith("h"):
        print("$20")
    else:
        print("$100")


main()