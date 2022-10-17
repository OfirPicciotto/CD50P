from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

def main():
    print(convert_date(input("Date of birth: ")))


def convert_date(dob):
    try:
         num_to_convert = str(datetime.strptime(str(date.today()), '%Y-%m-%d') - datetime.strptime(dob, '%Y-%m-%d')).split(" ")[0]
    except:
       return sys.exit("Invalid date")
    num_to_convert = str(int(num_to_convert) * 24 * 60)
    num_str = p.number_to_words(num_to_convert, andword="")
    return f"{num_str.capitalize()} minutes"

if __name__ == "__main__":
    main()