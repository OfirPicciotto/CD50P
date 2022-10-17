def main():
    user_input = input("Input time: ")
    convert(user_input)


def convert(time):
    suffix = None
    complete_time = time.split(" ")
    if len(complete_time) > 1:
        suffix = complete_time[1]
        hour, minute = complete_time[0].split(":")
    else:
        hour, minute = time.split(":")
    hour = int(hour)
    if (12 <= hour <= 13 and suffix is None) or (hour == 12 or hour == 1 and suffix == "pm"):
        print("lunch time")
    elif (18 <= hour <= 19 and suffix is None) or (6 <= hour <= 7 and suffix == "pm"):
        print("dinner time")
    elif (7 <= hour <= 8 and suffix is None) or (7 <= hour <= 8 and suffix == "am"):
        print("breakfast time")


if __name__ == "__main__":
    main()