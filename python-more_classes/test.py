Rectangle = __import__("3-rectangle").Rectangle

#!/usr/bin/python3

def test_rectangle():
    # Test 1: Création d'un carré avec une taille valide et position (0, 0)
    print("Test 1: Création d'un carré de taille 4")
    rectangle1 = Rectangle(4, 7)
    print(rectangle1)


if __name__ == "__main__":
    test_rectangle()
