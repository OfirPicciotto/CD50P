import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    is_valid_flag = True
    if 2 <= len(s) <= 6:
        for index, letter in enumerate(s):
            if (index == 0 or index ==1) and letter.isdigit() == True:
                is_valid_flag = False
            if not letter.isalpha() and not letter.isdigit():
                is_valid_flag = False
            if letter in string.punctuation:
                is_valid_flag = False
            if index+1 < len(s):
                if s[index].isdigit() and s[index+1].isalpha():
                     is_valid_flag = False
                if s[index].isalpha() and s[index+1] == "0":
                     is_valid_flag = False
        return  is_valid_flag


if __name__ == "__main__":
    main()