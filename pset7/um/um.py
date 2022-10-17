import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    for word in s.split(" "):
        if re.search(r"\bum\b", word.lower()):
            count += 1
    return count


if __name__ == "__main__":
    main()