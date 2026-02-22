#!/usr/bin/python3
def safe_print_list(my_list: list, x=0):
    printed_count = 0
    for i in range(x + 1):
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break

    return printed_count
