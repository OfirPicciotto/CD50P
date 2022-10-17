def main():
    adieu()


def adieu():
    names = []
    name_string = ""
    while True:
        try:
            name = input()
            names.append(name.strip())
        except EOFError:
            for index, n in enumerate(names):
                if (len(names) - 1) - index >= 1:
                    if len(names) > 2:
                        name_string += f"{n}, "
                    else:
                        name_string += f"{n} "
                elif (len(names) - 1) - index == 0 and len(names) > 1:
                    name_string += f"and {n}"
                else:
                    name_string = n
            print(f"Adieu, adieu, to {name_string}")
            break

main()