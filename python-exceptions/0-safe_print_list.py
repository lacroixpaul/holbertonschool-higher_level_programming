#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    counter = 0
    try:
        while i < x:
            print(my_list[i], end='')
            counter += 1
            i += 1
    except IndexError:
        pass
    print()
    return counter
