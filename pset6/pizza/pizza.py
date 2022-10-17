import sys
import csv
from tabulate import tabulate

if len(sys.argv) <= 1:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
else:
    file_name = sys.argv[1]
    rows = []
    if file_name.endswith(".csv"):
        try:
            with open(file_name) as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)
                print(tabulate(rows, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file")
