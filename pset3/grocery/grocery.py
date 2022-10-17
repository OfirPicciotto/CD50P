import collections
import sys


def main():
    grocery_list()


def grocery_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1
        except EOFError:
            break
    grocery_list = collections.OrderedDict(sorted(grocery_list.items()))
    for g_item in grocery_list:
        print(f"{grocery_list[g_item]} {g_item}")


main()
