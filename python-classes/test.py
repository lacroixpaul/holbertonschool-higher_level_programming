Square = __import__("6-square").Square

#!/usr/bin/python3

def test_square():
    # Test 1: Création d'un carré avec une taille valide et position (0, 0)
    print("Test 1: Création d'un carré de taille 4, position (0, 0)")
    square1 = Square(4, (0, 0))
    square1.my_print()
    print(f"Area: {square1.area()}")  # Devrait afficher 16

if __name__ == "__main__":
    test_square()
