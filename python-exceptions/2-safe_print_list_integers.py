#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print("IndexError: list index out of range")
            break
        i += 1
    print()
    return counter
