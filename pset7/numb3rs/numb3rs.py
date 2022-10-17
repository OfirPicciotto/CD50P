import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    ipLength = ip.split('.')
    if len(ipLength) > 4 or len(ipLength) <= 3:
        return False
    else:
        if re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
            return True
        else:
            return False

if __name__ == "__main__":
    main()