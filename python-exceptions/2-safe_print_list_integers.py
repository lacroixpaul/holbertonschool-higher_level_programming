#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        counter = 0
        while i < x:
            print("{:d}".format(my_list[i]))
            i += 1
            counter += 1
        return counter
    except (IndexError, ValueError, TypeError):
        return None
