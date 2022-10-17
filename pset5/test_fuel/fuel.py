def main():
    x = input("Level: ")
    print(convert(x))


def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        pctg = round((int(numerator)/int(denominator)) * 100)
    except ValueError:
        print("Invalid value, Try Again.")
    except ZeroDivisionError:
        print("Cant divide by zero, Try Again.")
    else:
        return gauge(pctg)


def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    elif 99 <= int(percentage) <= 100:
        return "F"
    # elif int(pctg) > 100:
    #     continue
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()