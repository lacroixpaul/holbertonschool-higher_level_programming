#!/usr/bin/python3

from pprint import pprint
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

if __name__ == "__main__":
    n = 5
    print(f"Pascal's Triangle for n = {n}:")
    pprint(pascal_triangle(n))

    n = 0
    print(f"\nPascal's Triangle for n = {n}:")
    pprint(pascal_triangle(n))

    n = -3
    print(f"\nPascal's Triangle for n = {n}:")
    pprint(pascal_triangle(n))

    n = 1
    print(f"\nPascal's Triangle for n = {n}:")
    pprint(pascal_triangle(n))

    n = 7
    print(f"\nPascal's Triangle for n = {n}:")
    pprint(pascal_triangle(n))
