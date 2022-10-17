from validator_collection import validators, checkers, errors
import sys

def main():
    print(validate_email(input("Email: ").strip()))

def validate_email(user_email):
    try:
        validators.email(user_email)
    except errors.EmptyValueError:
        sys.exit("Empty value")
    except errors.InvalidEmailError:
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()