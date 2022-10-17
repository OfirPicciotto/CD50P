def main():
    user_input = input("Input file name: ")
    file_extension(user_input)


def file_extension(file_name):
    if file_name.strip().lower().endswith(".gif"):
        print("image/gif")
    elif file_name.strip().lower().endswith(".jpg") or file_name.strip().lower().endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.strip().lower().endswith(".png"):
        print("image/png")
    elif file_name.strip().lower().endswith(".pdf"):
        print("application/pdf")
    elif file_name.strip().lower().endswith(".txt"):
        print("text/plain")
    elif file_name.strip().lower().endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()