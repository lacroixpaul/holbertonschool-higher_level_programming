#!/usr/bin/python3
import inspect
import hidden_4

if __name__ == "__main__":

    membres = inspect.getmembers(hidden_4, inspect.isfunction)
    noms_fonctions = sorted([nom for nom, _ in membres])
    for nom in noms_fonctions:
        if nom[0] != '_':
            print(nom)
