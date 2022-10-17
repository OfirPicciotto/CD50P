def main():
    user_input = input("Input a variable name: ")
    snake_case(user_input)


def snake_case(user_variable):
    new_var = ""
    for index, letter in enumerate(user_variable):
        print(index,letter)
        if letter.isupper():
            if index == 0:
                new_var += letter.lower()
            else:
                 new_var += f"_{letter.lower()}"
        else:
            new_var += letter
    print(new_var)

main()