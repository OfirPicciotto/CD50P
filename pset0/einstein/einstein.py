def main():
    c = 300000000 ** 2
    m = int(input("Input mass: "))
    calc_e(c, m)


def calc_e(c, m):
    print(c * m)


main()