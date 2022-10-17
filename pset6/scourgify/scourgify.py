import csv
import sys


if len(sys.argv) <= 1:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            with open(output_file, "w", newline='') as file1:
                    writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        row["first"] = row.pop("name")
                        first_name, last_name = row["first"].split(", ")
                        row["first"] = first_name
                        row["last"] = last_name
                        writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
