def main():
    x = check_fuel()
    print(x)


def check_fuel():
    while True:
        try:
            numerator, denominator = input("Enter a fraction: ").split("/")
            pctg = round((int(numerator)/int(denominator)) * 100)
        except ValueError:
            print("Invalid value, Try Again.")
        except ZeroDivisionError:
            print("Cant divide by zero, Try Again.")
        else:
            if int(pctg) <= 1:
                return "E"
            elif 99 <= int(pctg) <= 100:
                return "F"
            elif int(pctg) > 100:
                continue
            else:
                return f"{int(pctg)}%"

main()