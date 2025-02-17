import os
from task_03_xml import serialize_to_xml, deserialize_from_xml  # Assurez-vous d'importer vos fonctions depuis task_03_xml.py

def test_serialize_to_xml():
    # Dictionnaire d'exemple à sérialiser
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Paris",
        "height": 1.75
    }
    
    # Sérialiser le dictionnaire en XML
    filename = "data.xml"
    result = serialize_to_xml(data, filename)
    
    # Vérifier si la sérialisation a réussi
    if result:
        print(f"Sérialisation réussie ! Le fichier '{filename}' a été créé.")
    else:
        print("Erreur lors de la sérialisation.")
    
    return filename  # Retourner le nom du fichier pour la désérialisation

def test_deserialize_from_xml(filename):
    # Désérialiser les données du fichier XML
    result = deserialize_from_xml(filename)
    
    # Vérifier si la désérialisation a réussi
    if result:
        print("Désérialisation réussie ! Voici les données récupérées :")
        print(result)
    else:
        print("Erreur lors de la désérialisation.")
    
def main():
    # Tester la sérialisation
    filename = test_serialize_to_xml()
    
    # Tester la désérialisation
    test_deserialize_from_xml(filename)
    
    # Optionnel: Supprimer le fichier XML après le test
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Le fichier '{filename}' a été supprimé après le test.")

if __name__ == "__main__":
    main()
