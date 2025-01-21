#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            new_list.append(my_list_1[i] / my_list_2[i])
    except ZeroDivisionError:
        new_list[i] = 0
        print("division by 0")
    except TypeError:
        print("wrong type")
        new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        print("{}".format(new_list))
    return new_list
