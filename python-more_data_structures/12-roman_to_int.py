#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) == 0 or type(roman_string) is not str:
        return None
    roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    roman_numeral = 0
    i = 0
    while i < len(roman_string):
        current_value = roman_values[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = roman_values[roman_string[i + 1]]
            if current_value < next_value:
                roman_numeral += next_value - current_value
                i += 2
                continue
        roman_numeral += current_value
        i += 1
    return roman_numeral
