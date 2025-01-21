#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    max_number = a_dictionary[0]
    for i in range(len(a_dictionary)):
        if a_dictionary[i] > max_number:
            max_number = a_dictionary[i]
    return max_number
