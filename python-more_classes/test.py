#!/usr/bin/python3
Rectangle = __import__("3-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))  # Affiche le rectangle avec #
print("--")
print(my_rectangle)  # Utilise la méthode __str__
print("--")
print(repr(my_rectangle))  # Affiche la représentation de l'objet
print("--")
print(hex(id(my_rectangle)))  # Affiche l'adresse mémoire de l'objet
print("--")

# Créer une nouvelle instance en utilisant eval et repr
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))  # Affiche le rectangle du nouvel objet
print("--")
print(new_rectangle)  # Utilise la méthode __str__ pour afficher le rectangle
print("--")
print(repr(new_rectangle))  # Affiche la représentation du nouvel objet
print("--")
print(hex(id(new_rectangle)))  # Affiche l'adresse mémoire du nouvel objet
print("--")

# Comparaison pour vérifier que les objets ne sont pas identiques
print(new_rectangle is my_rectangle)  # False
print(type(new_rectangle) is type(my_rectangle))  # True
