import sys

count = 0


if len(sys.argv) == 1:
    sys.exit([1,"Too few command line arguments"])
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        file_name = sys.argv[1]
        try:
            with open(file_name) as file:
                for line in file:
                    if line.strip():
                        if not line.strip().startswith("#"):
                            count += 1
        except FileNotFoundError:
            sys.exit([1,"File does not exist"])
    else:
        sys.exit([1,"Not a python file"])
else:
    sys.exit([1,"Too many command line arguments"])

print(count)