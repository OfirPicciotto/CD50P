def main():
    comp_date()


def comp_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Enter Date: ").strip()
        try:
            m, d, y = date.split("/")
            if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                break
        except ValueError:
            try:
                str_m_d, y = date.split(",")
                str_m, str_d = str_m_d.split(" ")
                if str_m.title() in months:
                        m = months.index(str_m.title()) + 1
                d = str_d.replace(",", "")
                if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                    break
            except:
                print()
                pass
    print(f"{y}-{int(m):02}-{int(d):02}")


main()
