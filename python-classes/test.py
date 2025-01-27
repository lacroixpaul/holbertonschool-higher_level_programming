Square = __import__("2-square").Square

def test_square():
    try:
        # Test d'une instance valide
        square1 = Square(5)
        print(f"Carré de taille {square1._Square__size} créé avec succès.")
    except Exception as e:
        print(f"Erreur : {e}")
    try:
        # Test avec une taille négative (doit lever une exception ValueError)
        square3 = Square(-3)
    except Exception as e:
        print(f"Erreur : {e}")
        
test_square()
