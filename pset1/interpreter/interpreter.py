def main():
    user_input = input("Type an arithmetic expression: ")
    interpreter(user_input)

def interpreter(expression):
    print(float(eval(expression)))


main()